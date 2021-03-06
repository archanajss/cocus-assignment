# QA assignment for COCUS

## Task 1 โ RESTful API tests
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

 ๐ป LocalStack CLI 0.14.3.1

[22:05:58] starting LocalStack in Docker mode ๐ณ 
           preparing environment
           configuring container
           starting container
[22:06:00] detaching
```

* Query status of respective services on LocalStack by running
```
$ localstack status services
โโโโโโโโโโโโโโโโโโโโโโโโโโโโณโโโโโโโโโโโโโโ
โ Service                  โ Status      โ
โกโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโฉ
โ acm                      โ โ available โ
โ apigateway               โ โ available โ
โ cloudformation           โ โ available โ
โ cloudwatch               โ โ available โ
โ config                   โ โ available โ
โ dynamodb                 โ โ available โ
โ dynamodbstreams          โ โ available โ
โ ec2                      โ โ available โ
โ es                       โ โ available โ
โ events                   โ โ available โ
โ firehose                 โ โ available โ
โ iam                      โ โ available โ
โ kinesis                  โ โ available โ
โ kms                      โ โ available โ
โ lambda                   โ โ available โ
โ logs                     โ โ available โ
โ opensearch               โ โ available โ
โ redshift                 โ โ available โ
โ resource-groups          โ โ available โ
โ resourcegroupstaggingapi โ โ available โ
โ route53                  โ โ available โ
โ route53resolver          โ โ available โ
โ s3                       โ โ available โ
โ s3control                โ โ available โ
โ secretsmanager           โ โ available โ
โ ses                      โ โ available โ
โ sns                      โ โ available โ
โ sqs                      โ โ available โ
โ ssm                      โ โ available โ
โ stepfunctions            โ โ available โ
โ sts                      โ โ available โ
โ support                  โ โ available โ
โ swf                      โ โ available โ
โโโโโโโโโโโโโโโโโโโโโโโโโโโโดโโโโโโโโโโโโโโ
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
