from django.urls import path, reverse_lazy, include
from django_registration.backends.activation.views import RegistrationView

from .views import *
from .forms import RegisterForm

urlpatterns = [
    path('create/',
         RegistrationView.as_view(
             form_class=RegisterForm, success_url=reverse_lazy('django_registration_complete')
         ),
         name='register'
         ),
    path('', include('django_registration.backends.activation.urls')),
    path('', include('django.contrib.auth.urls')),
]
