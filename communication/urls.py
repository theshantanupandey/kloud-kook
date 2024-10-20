from django.urls import path
from .views import MessageListCreate, MessageDetail, TaskListCreate, TaskDetail

urlpatterns = [
    path('messages/', MessageListCreate.as_view(), name='message-list-create'),
    path('messages/<int:pk>/', MessageDetail.as_view(), name='message-detail'),
    path('tasks/', TaskListCreate.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
]