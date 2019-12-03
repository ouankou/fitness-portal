from django.test import TestCase
from portal.models import Client
from django.contrib.auth.models import User
from portal.api import program_list
from django.test.client import RequestFactory

class TestClient(TestCase):
    def setUp(self):
        self.client = Client()

    def test_program_list(self):
        print("testing program list")
        user = User(username = 'jax', email = 'jax@gmail.com', password = 'abc123456')
        user.is_staff = False
        user.first_name = 'Jacky'
        user.last_name = 'Smith'
        user.set_password('abc123456')
        user.save()
        client = Client.objects.create(
            user = user,
            purpose = 'rec',
            starting_weight = 150,
            current_weight = 200,
            target_weight = 160,
            blood_group = 'A',
            height_in_feet = 100,
            arm_size = 40,
            chest_size = 80,
            leg_size = 50,
            health_issues = 'None'
        )
        client.save()
        savedClient = Client.objects.filter(user__username='jax').first()
        request = RequestFactory().get('/program_list', {'client_id': savedClient.user_id})
        response = program_list(request)
        self.assertEquals(response.status_code, 200)
        print("PASS: the program list of a user is reviewed.")







