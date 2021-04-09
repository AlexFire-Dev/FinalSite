from django.contrib import admin

from .models import *


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)
    readonly_fields = ('created_at', 'modified_at')
