from django.test import TestCase,Client
from django.urls import resolve, reverse
from .views import *
from .api import *


class TestUrls(TestCase):
    def setUp(self):
        self.client=Client()

    def test_trainer_application_url(self):
        print("testing the trainer_application Url")
        url=reverse("trainer_application")
        result=resolve(url)
        self.assertEquals(result.func, trainer_application)
        print("PASS: trainer_application url is attached to a view")

    def test_client_signup_url(self):
        print("testing the client_signup Url")
        url=reverse("client_signup")
        result=resolve(url)
        self.assertEquals(result.func, client_signup)
        print("PASS: client_signup url is attached to a view")

    def test_login_url(self):
        print("testing the login Url")
        url = reverse("login")
        result = resolve(url)
        self.assertEquals(result.func, login)
        print("PASS: login url is attached to a view")

    def test_logout_url(self):
        print("testing the logout Url")
        url = reverse("logout")
        result = resolve(url)
        self.assertEquals(result.func, logout)
        print("PASS: logout url is attached to a view")

    def test_pending_trainer_applications_url(self):
        print("testing pending trainer_applications URL")
        url = reverse("pending_trainer_applications")
        result = resolve(url)
        self.assertEquals(result.func, pending_trainer_applications)
        print("PASS: pending_trainer_applications url is attached to a view")

    def test_trainer_application_decision_urls(self):
        print("testing trainer application decision URL")
        url = reverse("trainer_application_decision")
        result = resolve(url)
        self.assertEquals(result.func, trainer_application_decision)
        print("PASS: trainer_application_decision url is attached to a view")

    def test_add_program_urls(self):
        print("testing trainer application decision URL")
        url = reverse("add_program")
        result = resolve(url)
        self.assertEquals(result.func, add_program)
        print("PASS: add_program url is attached to a view")

    # path('programs/', program_list, name="program_list"),
    # path('program/<program_id>/<client_id>/', client_joining_program, name="client_joining_program"),
    # path('programs/client_subscribed/<client_id>/', get_client_subscribed_program_list, name="get_client_subscribed_program_list"),
