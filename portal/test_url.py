
from django.test import TestCase,Client
from django.urls import resolve, reverse
from portal import views

class TestUrls(TestCase):
    def setUp(self):
        self.client=Client()


    def test_trainer_application_url(self):
        print("testing the trainer_application Url")
        url=reverse("trainer_application")
        result=resolve(url)
        self.assertEquals(result.func,views.trainer_application)
        print("PASS: trainer_application url is attached to a view")


    def test_client_signup_url(self):
        print("testing the client_signup Url")
        url=reverse("client_signup")
        result=resolve(url)
        self.assertEquals(result.func,views.client_signup)
        print("PASS: client_signup url is attached to a view")

    def test_login_url(self):
        print("testing the login Url")
        url = reverse("login")
        result = resolve(url)
        self.assertEquals(result.func, views.login)
        print("PASS: login url is attached to a view")

    def test_logout_url(self):
        print("testing the logout Url")
        url = reverse("logout")
        result = resolve(url)
        self.assertEquals(result.func, views.logout)
        print("PASS: logout url is attached to a view")












