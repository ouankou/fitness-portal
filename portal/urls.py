from django.urls import path
from .views import *
from .api import *

urlpatterns = [
    path('', index, name='index'),
    path('trainer_application/', trainer_application, name='trainer_application'),
    path('trainer/pending_applications/', pending_trainer_applications, name='pending_trainer_applications'),
    path('trainer_application/<decision>/', trainer_application_decision, name='trainer_application_decision'),
    path('program/<trainer_username>/add/', add_program, name="add_program"),
    path('programs/', program_list, name="program_list"),
    path('program/<program_id>/<client_id>/', client_joining_program, name="client_joining_program"),
    path('programs/client_subscribed/<client_id>/', get_client_subscribed_program_list, name="get_client_subscribed_program_list"),
    path('client_signup/', client_signup, name='client_signup'),
    path('client/<username>/', render_client_index, name='client_profile'),
    path('trainer/<username>/', render_trainer_index, name='trainer_profile'),
    path('login/', login, name="login"),
    path('logout/', logout, name='logout')
]
