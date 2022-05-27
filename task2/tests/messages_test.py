import dataclasses
from json import dumps, loads
from pprint import pprint
from unicodedata import category
from unittest import TestCase

from models.car import Car
from utils.sqs import create_queue
from utils.sqs import delete_queue
from utils.sqs import delete_message
from utils.sqs import receive_messages
from utils.sqs import send_message

class SQSMessageTest(TestCase):

    __car_brands = []

    @classmethod
    def setup_class(cls):
        delete_queue()
        create_queue()

    def test_send_messages(self):
        # produce messages on sqs
        self.__add_cars_to_queue()
        # consume messages
        response = receive_messages()
        messages = response.get('Messages', [])
        for i,message in enumerate(messages):
            car = loads(message['Body'])
            self.assertIn(car['brand_name'], self.__car_brands)
            delete_message(message['ReceiptHandle'])

    def __add_cars_to_queue(self):
        for i in range(1, 3):
            car = Car(
                brand_name=f'brand{str(i)}', 
                model=f'model {str(i)}', 
                number_of_doors=4, 
                sports_car=False
            )
            self.__car_brands.append(car.brand_name);
            json_car = dumps(dataclasses.asdict(car))
            response = send_message(json_car)
            pprint(response)

    def get_message_by_id(messages, message_id):
        for message in messages:
            print(message['MessageId'])
            if message['MessageId'] == message_id:
                return message