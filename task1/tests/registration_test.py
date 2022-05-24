from json import dumps
from unittest import TestCase
from utils.request_helper import post

class TestRegistration(TestCase):
    def test_successful_registration(self):
        payload = dumps({
            'email': 'charles.morris@reqres.in',
            'password': 'test'
        })
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        response = post(path='register', payload=payload, headers=headers)
        self.assertEqual(response.status_code, 200)
        regDict = response.json()
        self.assertEqual(regDict['id'], 5)
        self.assertTrue(regDict['token'])

    def test_unsuccessful_registration(self):
        payload = dumps({
            'email': 'test',
            'password': 'test'
        })
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        response = post(path='register', payload=payload, headers=headers)
        self.assertEqual(response.status_code, 400)
        regDict = response.json()
        self.assertTrue(regDict['error'])