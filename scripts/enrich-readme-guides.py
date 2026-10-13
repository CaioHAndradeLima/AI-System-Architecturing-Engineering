#!/usr/bin/env python3
"""Expand ### guide blurbs in section READMEs from each linked doc's intro (2–3 sentences max)."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

GUIDE_BLOCK = re.compile(
    r"(### \[[^\]]+\]\(([^)]+)\)\n\n"
    r"(?:`[^`]+`(?: · `[^`]+`)*\n\n))"
    r"(.+?)"
    r"(\n\n→ \[See more)",
    re.DOTALL,
)


def extract_intro(md_path: Path) -> str | None:
    if not md_path.is_file():
        return None
    text = md_path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines:
        return None
    i = 1
    while i < len(lines) and not lines[i].strip():
        i += 1
    parts: list[str] = []
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            if parts:
                break
            i += 1
            continue
        if line.startswith("#") or line.startswith("```") or line.startswith("|"):
            break
        parts.append(line)
        i += 1
    if not parts:
        return None
    para = " ".join(parts)
    para = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", para)
    para = re.sub(r"\*\*([^*]+)\*\*", r"\1", para)
    para = re.sub(r"`([^`]+)`", r"\1", para)
    sents = re.split(r"(?<=[.!?])\s+", para)
    sents = [s.strip() for s in sents if len(s.strip()) > 10]
    if not sents:
        return None
    chosen = sents[:3]
    joined = " ".join(chosen)
    if len(joined) > 380:
        chosen = sents[:2]
        joined = " ".join(chosen)
    if len(joined) > 380:
        chosen = sents[:1]
    if len(chosen) == 1:
        return chosen[0]
    if len(chosen) == 2:
        return f"{chosen[0]}\n\n{chosen[1]}"
    return f"{chosen[0]}\n\n{chosen[1]}"


def should_replace(old: str, new: str) -> bool:
    old = old.strip()
    new = new.strip()
    if old == new:
        return False
    lines = [ln for ln in old.splitlines() if ln.strip()]
    # Keep polished multi-line blurbs that already have two substantive sentences
    if len(lines) >= 2 and len(old) > 160:
        return False
    return True


def process_readme(readme_path: Path) -> bool:
    content = readme_path.read_text(encoding="utf-8")
    base = readme_path.parent

    def replacer(m: re.Match[str]) -> str:
        prefix, link, old_desc, suffix = m.group(1), m.group(2), m.group(3), m.group(4)
        if link.startswith("http"):
            return m.group(0)
        target = (base / link.split("#")[0]).resolve()
        intro = extract_intro(target)
        if not intro:
            return m.group(0)
        if not should_replace(old_desc, intro):
            return m.group(0)
        return prefix + intro + suffix

    new_content = GUIDE_BLOCK.sub(replacer, content)
    if new_content != content:
        readme_path.write_text(new_content, encoding="utf-8")
        return True
    return False


def main() -> int:
    changed = 0
    for readme in sorted(ROOT.rglob("README.md")):
        if process_readme(readme):
            print(f"updated {readme.relative_to(ROOT)}")
            changed += 1
    print(f"done: {changed} README(s) updated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
