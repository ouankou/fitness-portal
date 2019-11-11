from django.urls import path
from .views import *
from .api import *

urlpatterns = [
    path('', index, name='index'),
    path('trainer_application/', trainer_application, name='trainer_application'),
    path('trainer/pending_applications/', pending_trainer_applications, name='pending_trainer_applications'),
    path('trainer_application/<decision>/', trainer_application_decision, name='trainer_application_decision'),
    path('client_signup/', client_signup, name='client_signup'),
    path('client/<username>/', render_client_index, name='client_profile'),
    path('trainer/<username>/', render_trainer_index, name='trainer_profile'),
    path('login/', login, name="login"),
    path('logout/', logout, name='logout')
]
