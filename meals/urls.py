from django.urls import path
from .views import MealListCreate, MealDetail

urlpatterns = [
    path('', MealListCreate.as_view(), name='meal-list-create'),
    path('<int:pk>/', MealDetail.as_view(), name='meal-detail'),
]