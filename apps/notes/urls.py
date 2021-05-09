from django.contrib.auth.decorators import login_required
from django.urls import path, reverse_lazy, include

from .views import *


urlpatterns = [
    path('', IndexView.as_view(), name='index'),

    path('<int:note>/', note_view, name='note'),
    path('<int:note>/change/', login_required(ChangeNoteView.as_view()), name='change-note'),
    path('<int:note>/delete/', login_required(note_delete_view), name='delete-note'),
    path('create/', login_required(CreateNote.as_view()), name='create-note'),

    path('favicon.ico/', IcoRedirect, name='ico')
]
