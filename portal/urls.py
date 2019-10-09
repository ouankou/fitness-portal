from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('trainer_application/', trainer_application, name='trainer_application'),
    path('client_signup/', client_signup, name='client_signup'),
    path('login/', login, name="login"),
    path('logout/', logout, name='logout')
]
