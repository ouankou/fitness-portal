from django.test import TestCase
from django.test import Client
from django.urls import reverse
import json


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()

    def test_trainer_application_view(self):
        print("testing the trainer_application View")
        response = self.client.get(reverse('trainer_application'))
        print(response)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "signups/trainer.html")

    def test_client_signupn_view(self):
        print("testing the client_signup View")
        response = self.client.get(reverse('client_signup'))
        print(response)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "signups/client.html")

    def test_homepage_view(self):
        print("testing the homepage View")
        response = self.client.get(reverse('index'))
        print(response)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "welcome.html")


    def test_login_view(self):
        print("testing the login View")
        response = self.client.get(reverse('login'))
        print(response)
        self.assertEquals(response.status_code, 400)

    def test_logout_view(self):
        print("testing the logout View")
        response = self.client.get(reverse('logout'))
        print(response)
        self.assertEquals(response.status_code, 302)







