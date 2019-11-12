import datetime
from dateutil.relativedelta import relativedelta
from django.db import models
from django.contrib.auth.models import User


class Trainer(models.Model):
    LOCATION_CHOICES_MAP = {
        'cherokee': "Cherokee",
        'mecklenburg': "Mecklenburg",
        'camden': "Camden",
        'moore': "Moore",
        'union': "Union",
        'cumberland': "Cumberland"
    }

    CERTIFICATION_CHOICE_MAP = {
        'nasm': 'NASM (National Academy of sports medicine)',
        'issa': 'ISSA (International Sports Sciences Association)',
        'ace': 'ACE (American Council on Exercise)',
        'acsm': 'ACSM (American College of Sports Medicine)',
        'nsca': 'NSCA (National Strength and Conditioning Association)'
    }

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)
    applied_on = models.DateField(auto_now_add=True, blank=True)
    approved_on = models.DateField(auto_now_add=True, blank=True)
    years_of_previous_experience = models.IntegerField(default=0)
    locations_served = models.CharField(max_length=255, default="", blank=True)
    charge = models.DecimalField(max_digits=5, decimal_places=2)
    certification = models.TextField(default="", blank=True)

    @property
    def full_name(self):
        return self.user.get_full_name()

    @property
    def years_of_experience_in_portal(self):
        experience_in_years = relativedelta(datetime.date.today() - self.approved_on).year
        return experience_in_years if experience_in_years else 0

    @property
    def years_of_overall_experience(self):
        return self.years_of_experience_in_portal + self.years_of_previous_experience

    @property
    def certification_list(self):
        cert_key_list = self.certification.split(",")
        cert_list = []
        for cert_key in cert_key_list:
            cert_list.append(self.CERTIFICATION_CHOICE_MAP[cert_key])
        return cert_list

    @property
    def certification_str(self):
        return ", ".join(self.certification_list)

    @property
    def location(self):
        return self.LOCATION_CHOICES_MAP[self.locations_served]

    @property
    def average_rating(self):
        # TODO calculate rating from child table
        return 0


class Client(models.Model):
    CLIENT_PURPOSE_CHOICES = [
        ('cmp', 'Competitive'),
        ('rec', 'Recreational')
    ]
    CLIENT_PURPOSE_CHOICE_MAP = {
        'cmp': "Competitive",
        'rec': "Recreational"
    }
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    purpose = models.CharField(max_length=100, choices=CLIENT_PURPOSE_CHOICES)
    starting_weight = models.DecimalField(max_digits=5, decimal_places=2)
    target_weight = models.DecimalField(max_digits=5, decimal_places=2)
    current_weight = models.DecimalField(max_digits=5, decimal_places=2)
    current_trainer = models.ForeignKey(Trainer, on_delete=models.SET_NULL, null=True)
    health_issues = models.TextField(default="", blank=True)
    blood_group = models.CharField(max_length=55)
    height_in_feet = models.DecimalField(max_digits=5, decimal_places=2)
    arm_size = models.DecimalField(max_digits=5, decimal_places=2)
    chest_size = models.DecimalField(max_digits=5, decimal_places=2)
    leg_size = models.DecimalField(max_digits=5, decimal_places=2)

    @property
    def purpose_text(self):
        return self.CLIENT_PURPOSE_CHOICE_MAP[self.purpose]

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name


class EmergencyContact(models.Model):
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.TextField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)


class TrainerRating(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    rating = models.IntegerField()
    rated_on = models.DateTimeField(auto_now_add=True, blank=True)


class Program(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=55, unique=True)
    overview = models.TextField()
    details = models.TextField()
    material_1 = models.TextField()
    material_2 = models.TextField(blank=True, null=True)
    material_3 = models.TextField(blank=True, null=True)
    created = models.DateField(auto_now_add=True, blank=True)
    is_active = models.BooleanField(default=True, blank=True)
