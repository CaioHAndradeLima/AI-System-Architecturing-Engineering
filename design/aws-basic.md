# AWS basic architecture

Single **Lambda** deployment with LangGraph supervisor and in-process specialist agents—good for prototypes and low traffic ([intermediate comparison](./aws-intermedium.md)).

```
                       USER
                         |
                         v
                 +---------------+
                 |  API Gateway  |
                 +---------------+
                         |
                         v
                 +---------------+
                 | AWS Lambda    |
                 | Python App    |
                 |                |
                 |  LangGraph     |
                 |                |
                 | +------------+ |
                 | | Supervisor | |
                 | +------------+ |
                 |    /     \     |
                 |   v       v    |
                 | +------+ +---+ |
                 | |Research| |Action|
                 | | Agent  | |Agent |
                 | +------+ +---+ |
                 +---------------+
                    |          |
                    v          v
              +--------------------+
              | Amazon Bedrock     |
              | LLM API            |
              +--------------------+
                    |
                    v
              +--------------------+
              | Output Validation  |
              | + Response         |
              +--------------------+
                    |
                    v
                   USER


     KNOWLEDGE (optional)

       +-------------+
       | Amazon S3   |
       | Documents   |
       +-------------+
              |
              v
       +--------------------+
       | Bedrock Knowledge  |
       | Base / Retrieval   |
       +--------------------+
              |
              v
        Research Agent


     OBSERVABILITY

       Lambda Logs / Metrics
                |
                v
         Amazon CloudWatch
```

## See also

- [AWS intermediate architecture](./aws-intermedium.md)
- [Design overview](./README.md)
