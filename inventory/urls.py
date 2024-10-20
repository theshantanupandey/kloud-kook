from django.urls import path
from .views import IngredientListCreate, IngredientDetail, SupplierListCreate, SupplierDetail

urlpatterns = [
    path('ingredients/', IngredientListCreate.as_view(), name='ingredient-list-create'),
    path('ingredients/<int:pk>/', IngredientDetail.as_view(), name='ingredient-detail'),
    path('suppliers/', SupplierListCreate.as_view(), name='supplier-list-create'),
    path('suppliers/<int:pk>/', SupplierDetail.as_view(), name='supplier-detail'),
]