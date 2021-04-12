from django.urls import path, reverse_lazy, include

from .views import *


urlpatterns = [
    path('', index_view, name='index'),
    path('<int:note>/', note_view, name='note')
]
