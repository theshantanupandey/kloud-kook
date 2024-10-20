from django.contrib import admin
from .models import Message, Task

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'content', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('sender__username', 'receiver__username', 'content')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('assignee', 'description', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'created_at', 'updated_at')
    search_fields = ('assignee__username', 'description')