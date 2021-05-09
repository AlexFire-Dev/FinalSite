from django import forms
from django_registration.forms import RegistrationForm

from apps.registration.models import User


class RegisterForm(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model = User


class ProfileChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'useGravatar')
