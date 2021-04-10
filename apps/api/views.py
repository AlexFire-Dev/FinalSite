from rest_framework.viewsets import ModelViewSet

from apps.notes.models import *
from .serializers import *


class NoteApiView(ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NotesSerializer
