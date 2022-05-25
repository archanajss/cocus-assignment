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
        self.assertEqual(regDict['token'], 'QpwL5tke4Pnpja7X5')

    def test_unsuccessful_registration(self):
        payload = dumps({
            'email': 'test@test.com',
            'password': 'test'
        })
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        response = post(path='register', payload=payload, headers=headers)
        self.assertEqual(response.status_code, 400)
        regDict = response.json()
        self.assertEqual(regDict['error'], 'Note: Only defined users succeed registration')

    def test_registration_empty_payload(self):
        payload = {}
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        response = post(path='register', payload=payload, headers=headers)
        self.assertEqual(response.status_code, 400)
        regDict = response.json()
        self.assertEqual(regDict['error'], 'Missing email or username')

    def test_registration_without_password(self):
        payload = dumps({
            'email': 'test@test.com'
        })
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        response = post(path='register', payload=payload, headers=headers)
        self.assertEqual(response.status_code, 400)
        regDict = response.json()
        self.assertEqual(regDict['error'], 'Missing password')

    def test_registration_blank_password(self):
        payload = dumps({
            'email': 'charles.morris@reqres.in',
            'password': ' '
        })
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        response = post(path='register', payload=payload, headers=headers)
        # expect API to return error for an empty or blank password. however, here it succeeds
        self.assertEqual(response.status_code, 200)
        regDict = response.json()
        self.assertEqual(regDict['id'], 5)
        self.assertEqual(regDict['token'], 'QpwL5tke4Pnpja7X5')

    def test_registration_cross_domain(self):
        payload = dumps({
            'email': 'charles.morris@reqres.in',
            'password': 'redirect:https://www.google.com/'
        })
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        response = post(path='register', payload=payload, headers=headers)
        # expect API to handle cross-domain injection attacks appropriately
        self.assertEqual(response.status_code, 200)
        regDict = response.json()
        self.assertEqual(regDict['id'], 5)
        self.assertEqual(regDict['token'], 'QpwL5tke4Pnpja7X5')

    def test_registration_sql_injection(self):
        payload = dumps({
            'email': 'charles.morris@reqres.in',
            'password': 'SELECT version();'
        })
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        response = post(path='register', payload=payload, headers=headers)
        # expect API to handle sql injection attacks appropriately
        self.assertEqual(response.status_code, 200)
        regDict = response.json()
        self.assertEqual(regDict['id'], 5)
        self.assertEqual(regDict['token'], 'QpwL5tke4Pnpja7X5')