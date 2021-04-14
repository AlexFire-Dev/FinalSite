from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, TemplateView
import requests

from .models import Note
from .forms import CreateNoteForm


class IndexView(TemplateView):
    template_name = 'notes/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        section = self.request.GET.get('section')
        search = self.request.GET.get('search', '')

        if section == 'public-notes':
            notes = Note.objects.filter(status=True)
        elif section == 'my-notes':
            notes = Note.objects.filter(author=self.request.user)
        else:
            notes = Note.objects.filter(Q(status=True) | Q(author=self.request.user))

        if search != '':
            notes = notes.filter(Q(title__contains=search) | Q(text__contains=search))

        context.update({
            'notes': notes,
            'section': section,
            'search': search,
        })
        return context


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
