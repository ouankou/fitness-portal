from django.test import TestCase
from portal.models import Client
from django.contrib.auth.models import User

class TestClient(TestCase):
    def setUp(self):
        self.client = Client()

    def test_client_creation(self):
        print("testing user creation")
        user = User(username = 'jax', email = 'jax@gmail.com', password = 'abc123456')
        user.is_staff = False
        user.first_name = 'Jacky'
        user.last_name = 'Smith'
        user.set_password('abc123456')
        user.save()
        savedUser = User.objects.filter(username='jax').first()
        self.assertEquals(user, savedUser)
        print("testing client creation")
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
        savedClient = Client.objects.filter(user__username = 'jax').first()
        self.assertEquals(client, savedClient)
        self.assertEquals(savedClient.user.is_staff, False)
        print("PASS: a client entry is created in the database")







