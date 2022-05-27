from pprint import pprint
import boto3

from config import ENDPOINT_URL

def send_message(msg):
    pprint(msg)
    sqs_client = boto3.client('sqs', aws_access_key_id='secret_id', aws_secret_access_key='secret_key', endpoint_url=ENDPOINT_URL)
    response = sqs_client.send_message(
        QueueUrl=get_queue_url(sqs_client),
        MessageBody=(msg)
    )
    pprint(response)
    return response

def receive_messages():
    sqs_client = boto3.client('sqs', aws_access_key_id='secret_id', aws_secret_access_key='secret_key', endpoint_url=ENDPOINT_URL)
    messages = sqs_client.receive_message(
        QueueUrl=get_queue_url(sqs_client),
        MaxNumberOfMessages=10,
        WaitTimeSeconds=10
    )
    pprint(messages)
    return messages

def delete_message(receipt_handle):
    sqs_client = boto3.client('sqs', aws_access_key_id='secret_id', aws_secret_access_key='secret_key', endpoint_url=ENDPOINT_URL)
    response = sqs_client.delete_message(
        QueueUrl=get_queue_url(sqs_client),
        ReceiptHandle=receipt_handle
    )
    pprint(response)

def create_queue():
    sqs_client = boto3.client('sqs', aws_access_key_id='secret_id', aws_secret_access_key='secret_key', endpoint_url=ENDPOINT_URL)
    response = sqs_client.create_queue(
        QueueName='cars',
        Attributes={
            'DelaySeconds': '0',
            'VisibilityTimeout': '60',
        }
    )
    pprint(response)

def delete_queue():
    sqs_client = boto3.client('sqs', aws_access_key_id='secret_id', aws_secret_access_key='secret_key', endpoint_url=ENDPOINT_URL)
    response = sqs_client.delete_queue(
        QueueUrl=get_queue_url(sqs_client)
    )

def get_queue_url(sqs_client):
    response = sqs_client.get_queue_url(
        QueueName='cars'
    )
    return response['QueueUrl']

def purge_queue():
    sqs_client = boto3.client('sqs', aws_access_key_id='secret_id', aws_secret_access_key='secret_key', endpoint_url=ENDPOINT_URL)
    sqs_client.purge_queue(
        QueueUrl=get_queue_url(sqs_client)
    )