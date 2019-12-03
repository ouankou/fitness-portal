from django.test import TestCase
from portal.models import Trainer
from django.contrib.auth.models import User
from portal.api import pending_trainer_applications
from django.test.client import RequestFactory

class TestTrainer(TestCase):
    def setUp(self):
        self.trainer = Trainer()

    def test_pending_trainer_applications(self):
        print("testing pending trainer applications")
        user = User(username = 'jax', email = 'jax@gmail.com', password = 'abc123456')
        user.is_staff = True
        user.first_name = 'Jacky'
        user.last_name = 'Smith'
        user.set_password('abc123456')
        user.save()
        trainer = Trainer.objects.create(
            user = user,
            years_of_previous_experience = 4,
            charge = 200,
            locations_served = 'union',
            certification = 'ace'
        )
        trainer.save()
        request = RequestFactory().get('/trainer/pending_applications')
        response = pending_trainer_applications(request)
        self.assertEquals(response.status_code, 200)
        print("PASS: the list of pending trainer applications is reviewed.")







