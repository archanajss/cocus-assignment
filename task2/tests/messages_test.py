import dataclasses
from json import dumps
from pprint import pprint
from unittest import TestCase

from models.car import Car
from utils.sqs_helper import delete_message
from utils.sqs_helper import purge_queue
from utils.sqs_helper import produce_message

class SQSMessageTest(TestCase):
    
    @classmethod
    def setup_class(cls):
        purge_queue()

    @classmethod
    def teardown_class(cls):
        purge_queue()

    def test_produce_messages(self):
        car = Car(brand_name='bmw', model='2 Series', number_of_doors=5, sports_car=False)
        json_car = dumps(dataclasses.asdict(car))
        response = produce_message(json_car)
        pprint(response)
        message_id = response['MessageId']
        message = self.get_message_by_id(messages=response, message_id=message_id)
        self.assertTrue(message)
        pprint(message['Body'])
        delete_message(message_id)

    def get_message_by_id(messages, message_id):
        for message in messages:
            if message['MessageId'] == message_id:
                return message