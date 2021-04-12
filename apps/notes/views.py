from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
import requests

from .models import Note


def index_view(request):

    context = {
        'notes': Note.objects.all()
    }
    return render(request, 'notes/index.html', context=context)


def note_view(request, note: int):

    context = {
        'note': Note.objects.get(id=note)
    }
    return render(request, 'notes/one-note.html', context=context)
