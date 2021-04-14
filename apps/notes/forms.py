from django import forms

from apps.notes.models import Note


class CreateNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'text', 'status')
