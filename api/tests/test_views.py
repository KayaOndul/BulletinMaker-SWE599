import json

from django.test import Client, TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory

client = Client()


class TestUserEndpoints(TestCase):

    def setUp(self):
        self.invalid_payload = {
            'username': 'test1',
            'password': 'pass',
            'password2': 'pasd',
            'email': 'test@mail.com'
        }

    def returnNotValidIfPasswordsDoesntMatch(self):
        response = APIRequestFactory().post(path="api/users/")
        data=json.dumps(self.invalid_payload)
        content_type='application/json'

        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
