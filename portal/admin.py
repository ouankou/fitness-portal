from django.contrib import admin
from .models import *


class TrainerAdmin(admin.ModelAdmin):
    list_display = [
        "user", "applied_on", "approved_on", "years_of_previous_experience", "locations_served",
        "charge", "certification", "is_approved"
    ]


class ClientAdmin(admin.ModelAdmin):
    list_display = [
        "user", "purpose", "starting_weight", "current_weight", "current_trainer", "health_issues", "blood_group",
        "height_in_feet", "arm_size", "chest_size", "leg_size"
    ]


class EmergencyContactAdmin(admin.ModelAdmin):
    list_display = [
        "client", "name", "number", "email", "address"
    ]


class TrainerRatingAdmin(admin.ModelAdmin):
    list_display = [
        "trainer", "client", "rating", "rated_on"
    ]


class ActivitiesAdmin(admin.ModelAdmin):
    list_display = [
        "name", "category", "reference_material", "created_by", "status"
    ]


class ChallengesAdmin(admin.ModelAdmin):
    list_display = ["name", "created_by"]


class ChallengedActivitiesAdmin(admin.ModelAdmin):
    list_display = ["challenge", "activity", "status"]


class AssignedChallengesToClientAdmin(admin.ModelAdmin):
    list_display = ["client", "assigned_by", "routine_type", "start_date", "end_date"]


admin.site.register(Trainer, TrainerAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(EmergencyContact, EmergencyContactAdmin)
admin.site.register(TrainerRating, TrainerRatingAdmin)
admin.site.register(Activities, ActivitiesAdmin)
admin.site.register(Challenges, ChallengesAdmin)
admin.site.register(ChallengedActivities, ChallengedActivitiesAdmin)
admin.site.register(AssignedChallengesToClient, AssignedChallengesToClientAdmin)
admin.site.site_header = "FITNESS PORTAL ADMIN"
