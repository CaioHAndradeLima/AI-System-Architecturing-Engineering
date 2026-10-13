                         USERS
                           |
                           v
                   +---------------+
                   | API Gateway   |
                   +---------------+
                           |
                           v
                   +---------------+
                   | ALB           |
                   +---------------+
                           |
                           v
              +-------------------------+
              | ECS Fargate             |
              |                         |
              | +---------------------+ |
              | | Supervisor Service  | |
              | | LangGraph            | |
              | +---------------------+ |
              +-------------------------+
                           |
               +-----------+-----------+
               |                       |
               v                       v
     +-------------------+   +-------------------+
     | Research Service  |   | Action Service    |
     | ECS Fargate       |   | ECS Fargate       |
     +-------------------+   +-------------------+
               |                       |
               v                       v
     +-------------------+   +-------------------+
     | Vector Retrieval  |   | External Business |
     | / Knowledge Base  |   | APIs               |
     +-------------------+   +-------------------+
               |
               v
     +-------------------+
     | Amazon Bedrock    |
     +-------------------+


      ASYNC TASK PROCESSING

     +-------------------+
     | Supervisor / API   |
     +-------------------+
               |
               v
     +-------------------+
     | Amazon SQS        |
     | Work Queue        |
     +-------------------+
               |
               v
     +-------------------+
     | ECS Worker        |
     | Background Jobs   |
     +-------------------+


      STATE AND KNOWLEDGE

     +-------------------+     +-------------------+
     | Amazon DynamoDB   |     | Amazon S3         |
     | Workflow State    |     | Documents         |
     +-------------------+     +-------------------+


      OBSERVABILITY

     ECS + ALB + Bedrock
               |
               v
     +-------------------+
     | CloudWatch        |
     | Metrics / Logs    |
     +-------------------+
               |
               v
     +-------------------+
     | Alarms / Alerts   |
     +-------------------+


