from django.db import models

from apps.registration.models import User


class Note(models.Model):
    title = models.CharField(max_length=40)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
