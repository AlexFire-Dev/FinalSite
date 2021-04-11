from django.urls import path, reverse_lazy, include
from rest_framework import routers

from .views import *


router = routers.SimpleRouter()

router.register(r'note', NoteApiView)
router.register(r'user', UserApiView)

urlpatterns = [
    path('', include(router.urls))
]
