from django.urls import path
from .views import UserCreate

urlpatterns = [
    path('register/', UserCreate.as_view(), name='register'),
    path('enable-two-factor/', enable_two_factor, name='enable_two_factor'),
]