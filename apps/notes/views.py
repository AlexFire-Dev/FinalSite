from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
import requests

from .models import Note
from .forms import CreateNoteForm


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


class CreateNote(CreateView):

    form_class = CreateNoteForm
    template_name = 'notes/create_note.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):

        args = {
            'title': form.cleaned_data['title'],
            'text': form.cleaned_data['text'],
            'author_id': self.request.user.id,
            'status': form.cleaned_data['status'],
        }
        Note.objects.create(**args)
        return HttpResponseRedirect(self.success_url)
