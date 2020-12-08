from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Credential
from rest_framework.test import force_authenticate
from rest_framework.test import APIRequestFactory
from .views import search

factory = APIRequestFactory()


class SearchTest(APITestCase):
    def test_search(self):
        url = factory.get(reverse(search))
        force_authenticate(url)
        response = search(url)
        self.assertEqual(response.status_code, 200)


class CredentialTest(TestCase):
    def setUp(self):
        Credential.objects.create(
            client_id='abcd',
            client_secret='1234'
        )

    def test_credential(self):
        user = Credential.objects.get(client_id='abcd')
        self.assertEqual(user.client_secret, '1234')
