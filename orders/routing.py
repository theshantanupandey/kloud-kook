from django.urls import path
from .consumers import OrderStatusConsumer

websocket_urlpatterns = [
    path('ws/order-status/', OrderStatusConsumer.as_asgi()),
]