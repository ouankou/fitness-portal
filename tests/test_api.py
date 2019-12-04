from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase,Client
from django.test import Client as clientobject
from django.urls import resolve, reverse
from .models import Client
from .views import *
from .api import *
import requests
import json
import unittest




class Test_APIs(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test',
                                                         password='12test12',
                                                         email='test@example.com')

        self.clientuserobject = get_user_model().objects.create_user(username='testcleint',
                                                         password='12test12',
                                                         email='testcleint@example.com')

        self.traineruserobject = get_user_model().objects.create_user(username='testtrainer',
                                                         password='12test12',
                                                         email='testtrainer@example.com')



        self.client=clientobject()
        self.rf = RequestFactory()
        self.clientuser= Client.objects.create(

            user=self.clientuserobject,
            purpose='rec',
            starting_weight='70',
            current_weight='65',
            target_weight='60',
            blood_group='AB',
            height_in_feet='6',
            arm_size='15',
            chest_size='42',
            leg_size='18',
            health_issues='none'
        )
        self.clientuser.save()


        self.trainer=Trainer.objects.create(

            user=self.traineruserobject,
            years_of_previous_experience=5,
            charge=100,
            locations_served="charlotte",
            certification="ace"
            )

        self.trainer.save()

        self.demoprogram=Program.objects.create(
            trainer=self.trainer,
            name="workout1",
            code='upperbody_1',
            overview="upperbodyworkout",
            details="program for upper body",
            material_1="bench press",
            material_2="pushups",
            material_3="burpee"
        )
        self.demoprogram.save()

        self.client_subscribed_program = ClientSubscribedProgram.objects.create(
            program_id=self.demoprogram.id,
            client_id=self.clientuser.id
        )
        self.client_subscribed_program.save()



    def test_correctcredentiails(self):

        data = {'username': 'test', 'password': '12test12'}
        response=self.client.post(reverse('login'),data,content_type='application/json')
        print(response)
        self.assertEquals(response.status_code,200)
        response_data=response.json()
        self.assertEqual(response_data['is_authenticated'],True)



    def test_badcredentiails(self):
        data = {'username': 'tes', 'password': '12test12'}
        response = self.client.post(reverse('login'), data, content_type='application/json')
        print(response)
        self.assertEquals(response.status_code, 200)
        response_data = response.json()
        self.assertEqual(response_data['is_authenticated'],False)

    def test_api(self):

        ########call the api function using clientid as paramter ###########
        response=get_client_subscribed_program_list_(self.clientuser.id)
        print("program data",response)

        ######verify the api output data###################
        self.assertEquals(response["data"][0][1],"workout1")
        self.assertEquals(response["data"][0][2], "upperbody_1")
        self.assertEquals(response["data"][0][4], "upperbodyworkout")

    def test_trainercertifcation(self):
        response=self.trainer.certification_list
        self.assertEqual(response[0],'ACE (American Council on Exercise)')

    def test_years_of_experience_in_portal(self):
        response= self.trainer.years_of_overall_experience
        self.assertEqual(response,5)

    def test_cleinttype_function(self):
        response=self.clientuser.purpose_text
        self.assertEqual(response,"Recreational")

    def test_client_signup(self):
        data="first_name=test&last_name=test&username=testdjango15&password=&password=&" \
             "email=sumeet.mehta91%40gmail.com&purpose=rec&current_weight=1&target_weight=1&blood_group=ab&height_in_feet=1" \
             "&arm_size=1&chest_size=1&leg_size=1&health_issues=no"
        #data = json.dumps(data)
        response1 = self.client.post(reverse('client_signup'), data,content_type='application/x-www-form-urlencoded')
        self.assertEqual(response1.status_code,200)

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


    def tearDown(self):
        self.user.delete()
