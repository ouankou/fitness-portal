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
        self.assertEquals(client.user, user)
        self.assertEquals(client.purpose, 'rec')
        self.assertEquals(client.starting_weight, 150)
        self.assertEquals(client.current_weight, 200)
        self.assertEquals(client.target_weight, 160)
        self.assertEquals(client.blood_group, 'A')
        self.assertEquals(client.height_in_feet, 100)
        self.assertEquals(client.arm_size, 40)
        self.assertEquals(client.chest_size, 80)
        self.assertEquals(client.leg_size, 50)
        self.assertEquals(client.health_issues, 'None')
        print("PASS: an instance of Client class is created.")







