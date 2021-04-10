from django.urls import path, reverse_lazy, include
from rest_framework import routers

from .views import *


router = routers.SimpleRouter()

router.register(r'notes', NoteApiView)

urlpatterns = [
    path('', include(router.urls))
]
