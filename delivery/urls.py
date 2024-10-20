from django.urls import path
from .views import DeliveryListCreate, DeliveryDetail

urlpatterns = [
    path('', DeliveryListCreate.as_view(), name='delivery-list-create'),
    path('<int:pk>/', DeliveryDetail.as_view(), name='delivery-detail'),
    path('optimize-route/', optimize_route, name='optimize-route'),
    path('track-delivery/', track_delivery, name='track-delivery'),
]