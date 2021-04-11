from rest_framework.serializers import ModelSerializer

from apps.notes.models import Note
from apps.registration.models import User


class NotesSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'is_active')
