# QA assignment for COCUS

## Task 1 – RESTful API tests
### Prerequisites
Install prerequisites using requirements file by running this command from `task1` directory
```
$ pip3 install -r requirements.txt
```

### Run tests
For runnning tests of tasks 1, run the command from `task1/tests` folder
```
$ pytest -s .
```

Tests should run successfully generating the test output


## Task 2 - Stream processing test
### Setup
* Install Docker Desktop from Docker
* Install aws-cli from AWS
* Pull LocalStack image
```
$ docker pull localstack/localstack
```
* Start LocalStack in docker container using command
```
$ localstack start -d

     __                     _______ __             __
    / /   ____  _________ _/ / ___// /_____ ______/ /__
   / /   / __ \/ ___/ __ `/ /\__ \/ __/ __ `/ ___/ //_/
  / /___/ /_/ / /__/ /_/ / /___/ / /_/ /_/ / /__/ ,<
 /_____/\____/\___/\__,_/_//____/\__/\__,_/\___/_/|_|

 💻 LocalStack CLI 0.14.3.1

[22:05:58] starting LocalStack in Docker mode 🐳 
           preparing environment
           configuring container
           starting container
[22:06:00] detaching
```

* Query status of respective services on LocalStack by running
```
$ localstack status services
┏━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━┓
┃ Service                  ┃ Status      ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━┩
│ acm                      │ ✔ available │
│ apigateway               │ ✔ available │
│ cloudformation           │ ✔ available │
│ cloudwatch               │ ✔ available │
│ config                   │ ✔ available │
│ dynamodb                 │ ✔ available │
│ dynamodbstreams          │ ✔ available │
│ ec2                      │ ✔ available │
│ es                       │ ✔ available │
│ events                   │ ✔ available │
│ firehose                 │ ✔ available │
│ iam                      │ ✔ available │
│ kinesis                  │ ✔ available │
│ kms                      │ ✔ available │
│ lambda                   │ ✔ available │
│ logs                     │ ✔ available │
│ opensearch               │ ✔ available │
│ redshift                 │ ✔ available │
│ resource-groups          │ ✔ available │
│ resourcegroupstaggingapi │ ✔ available │
│ route53                  │ ✔ available │
│ route53resolver          │ ✔ available │
│ s3                       │ ✔ available │
│ s3control                │ ✔ available │
│ secretsmanager           │ ✔ available │
│ ses                      │ ✔ available │
│ sns                      │ ✔ available │
│ sqs                      │ ✔ available │
│ ssm                      │ ✔ available │
│ stepfunctions            │ ✔ available │
│ sts                      │ ✔ available │
│ support                  │ ✔ available │
│ swf                      │ ✔ available │
└──────────────────────────┴─────────────┘
```

* Create an SQS queue on LocalStack named "cars"
```
$ aws --endpoint-url=http://localhost:4566 sqs create-queue --queue-name cars
{
    "QueueUrl": "http://localhost:4566/000000000000/cars"
}

```

* Configure aws using command
```
$ aws configure
AWS Access Key ID [None]: <your_secret_id>
AWS Secret Access Key [None]: <your_secret_key>
Default region name [None]: us-east-1
Default output format [None]: json
```

### Run tests
For runnning tests of tasks 2, run the command from `task2/tests` folder
```
$ pytest -s .
```

Tests should run successfully generating the test output
