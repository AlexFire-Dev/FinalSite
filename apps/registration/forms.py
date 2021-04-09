from django import forms
from django_registration.forms import RegistrationForm

from apps.registration.models import User


class RegisterForm(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model = User
