from pprint import pprint
import boto3

from config import QUEUE_URL
from config import ENDPOINT_URL

def produce_message(msg):
    sqs = boto3.client('sqs', aws_access_key_id='secret_id', aws_secret_access_key='secret_key', endpoint_url=ENDPOINT_URL)
    response = sqs.send_message(
        QueueUrl=QUEUE_URL,
        MessageBody=(msg)
    )
    pprint(response)
    return response

def consume_message():
    sqs = boto3.resource('sqs', aws_access_key_id='secret_id', aws_secret_access_key='secret_key', endpoint_url=ENDPOINT_URL)
    cars_queue = sqs.get_queue_by_name(QueueName='cars')
    messages = cars_queue.receive_messages()
    pprint(messages)
    return messages

def delete_message(receipt_handle):
    sqs = boto3.client('sqs', aws_access_key_id='secret_id', aws_secret_access_key='secret_key', endpoint_url=ENDPOINT_URL)
    response = sqs.client.delete_message(
        QueueUrl=QUEUE_URL,
        ReceiptHandle=receipt_handle
    )
    pprint(response)

def purge_queue():
    sqs = boto3.client('sqs', aws_access_key_id='secret_id', aws_secret_access_key='secret_key', endpoint_url=ENDPOINT_URL)
    sqs.purge_queue(QueueUrl=QUEUE_URL)