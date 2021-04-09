from django.urls import path, reverse_lazy, include
from django_registration.backends.one_step.views import RegistrationView

from .views import *
from .forms import RegisterForm

urlpatterns = [
    path('create/',
         RegistrationView.as_view(
             form_class=RegisterForm, success_url=reverse_lazy('index')
         ),
         name='register'
         ),
    path('', include('django_registration.backends.one_step.urls')),
    path('', include('django.contrib.auth.urls')),
]
