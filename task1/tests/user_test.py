from unittest import TestCase
from utils.request_helper import get

class TestUsers(TestCase):
    def test_list_users(self):
        response = get(path='users')
        self.assertEqual(response.status_code, 200)
        users = response.json()
        self.assertTrue(len(users) != 0)
