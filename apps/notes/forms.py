from django import forms

from apps.notes.models import Note


class CreateNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'text', 'status')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.CheckboxInput(attrs={'class': 'form-check'}),
        }
