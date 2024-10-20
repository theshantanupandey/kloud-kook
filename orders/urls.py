from django.urls import path
from .views import OrderListCreate, OrderDetail

urlpatterns = [
    path('', OrderListCreate.as_view(), name='order-list-create'),
    path('<int:pk>/', OrderDetail.as_view(), name='order-detail'),
]