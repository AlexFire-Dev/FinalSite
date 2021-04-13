from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import TemplateView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import *
from rest_framework.permissions import *
from rest_framework.authtoken.models import Token

from apps.notes.models import *
from apps.registration.models import *
from .serializers import *


class DeveloperToken(TemplateView):
    template_name = 'api/developers.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if Token.objects.filter(user=self.request.user):
            token = Token.objects.get(user=self.request.user)
        else:
            token = 'Ещё не создан!'

        context.update({
            'token': token,
        })
        return context


class UserApi(ListAPIView):
    """Пользователи"""

    permission_classes = [IsAdminUser]
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['id', 'username', 'first_name', 'last_name']
    search_fields = ['username', 'first_name', 'last_name']
    ordering_fields = ['id', 'username', 'first_name', 'last_name']

    def get_queryset(self):

        queryset = User.objects.all()
        return queryset


class NoteApi(ListAPIView):
    """Заметки"""

    permission_classes = [IsAuthenticated]
    serializer_class = NotesSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['id', 'title', 'author', 'status']
    search_fields = ['title', 'text']
    ordering_fields = ['id', 'title']

    def get_queryset(self):

        query_set = Note.objects.all()
        return query_set


def CreateToken(request):

    Token.objects.get_or_create(user=request.user)
    return redirect(reverse('developer-portal'))
