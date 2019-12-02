from django.test import TestCase
from portal.models import Trainer
from django.contrib.auth.models import User

class TestTrainer(TestCase):
    def setUp(self):
        self.trainer = Trainer()

    def test_trainer_creation(self):
        print("testing user creation")
        user = User(username = 'jax', email = 'jax@gmail.com', password = 'abc123456')
        user.is_staff = True
        user.first_name = 'Jacky'
        user.last_name = 'Smith'
        user.set_password('abc123456')
        user.save()
        savedUser = User.objects.filter(username='jax').first()
        self.assertEquals(user, savedUser)
        print("testing trainer creation")
        trainer = Trainer.objects.create(
            user = user,
            years_of_previous_experience = 4,
            charge = 200,
            locations_served = 'union',
            certification = 'ace'
        )
        self.assertEquals(trainer.user, user)
        self.assertEquals(trainer.years_of_previous_experience, 4)
        self.assertEquals(trainer.charge, 200)
        self.assertEquals(trainer.locations_served, 'union')
        self.assertEquals(trainer.certification, 'ace')
        print("PASS: an instance of Trainer class is created.")







