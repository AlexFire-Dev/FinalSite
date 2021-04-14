from django.contrib.auth.decorators import login_required
from django.urls import path, reverse_lazy, include

from .views import *


urlpatterns = [
    path('', index_view, name='index'),
    path('<int:note>/', note_view, name='note'),
    path('create/', login_required(CreateNote.as_view()), name='create-note'),
]
