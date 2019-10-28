import datetime
from dateutil.relativedelta import relativedelta
from django.db import models
from django.contrib.auth.models import User


class Trainer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)
    applied_on = models.DateField(auto_now_add=True, blank=True)
    approved_on = models.DateField(auto_now_add=True, blank=True)
    years_of_previous_experience = models.IntegerField(default=0)
    locations_served = models.TextField(default="", blank=True)
    charge = models.DecimalField(max_digits=5, decimal_places=2)  # per week
    certification = models.TextField(default="", blank=True)

    @property
    def years_of_experience_in_portal(self):
        return relativedelta(datetime.date.today() - self.approved_on).year

    @property
    def years_of_overall_experience(self):
        return self.years_of_experience_in_portal + self.years_of_previous_experience

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


class Activities(models.Model):
    ACTIVITY_CATEGORY_CHOICES = [
        ('w', 'Weight'),
        ('c', 'Cardio')
    ]
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=55, choices=ACTIVITY_CATEGORY_CHOICES)
    reference_material = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    status = models.BooleanField(default=True)


class Challenges(models.Model):
    name = models.CharField(max_length=55)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


class ChallengedActivities(models.Model):
    challenge = models.ForeignKey(Challenges, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activities, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)


class AssignedChallengesToClient(models.Model):
    ROUTINE_TYPE_CHOICES = [
        ('d', "Daily"),
        ('w', "Weekly"),
        ('m', "Monthly"),
    ]
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    assigned_by = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    routine_type = models.CharField(max_length=55, choices=ROUTINE_TYPE_CHOICES)
    start_date = models.DateField(auto_now_add=True, blank=True)
    end_date = models.DateField(auto_now_add=True, blank=True)
