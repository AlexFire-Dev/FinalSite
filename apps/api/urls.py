from django.urls import path, reverse_lazy, include
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib.auth.decorators import login_required

from .views import *


urlpatterns = [
    path('note/', NoteApi.as_view(), name='get-notes'),
    path('user/', UserApi.as_view(), name='get-users'),

    path('developers/', login_required(DeveloperToken.as_view()), name='developer-portal'),
    path('developers/token-create/', login_required(CreateToken), name='token_create'),
]
