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


class ProgramAdmin(admin.ModelAdmin):
    list_display = ['trainer', 'name', 'code', 'overview', 'details', 'material_1', 'material_2', 'material_3',
                    'created', 'is_active']


admin.site.register(Trainer, TrainerAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(EmergencyContact, EmergencyContactAdmin)
admin.site.register(TrainerRating, TrainerRatingAdmin)
admin.site.register(Program, ProgramAdmin)
admin.site.site_header = "FITNESS PORTAL ADMIN"
