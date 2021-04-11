from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import *
from rest_framework.viewsets import ModelViewSet

from apps.notes.models import *
from apps.registration.models import *
from .serializers import *


class NoteApiView(ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NotesSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['id', 'title', 'author', 'status']
    search_fields = ['title', 'text']
    ordering_fields = ['id', 'title']


class UserApiView(ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['id', 'username', 'first_name', 'last_name']
    search_fields = ['username', 'first_name', 'last_name']
    ordering_fields = ['id', 'username', 'first_name', 'last_name']
