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


