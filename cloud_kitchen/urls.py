from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('accounts/', include('allauth.urls')),
    path('api/communication/', include('communication.urls')),
    path('api/', include('api.urls')),
    path('pos/', application.urls),
    path('api/orders/', include('orders.urls')),
    path('api/meals/', include('meals.urls')),
    path('api/inventory/', include('inventory.urls')),
    path('api/deliveries/', include('delivery.urls')),
    path('api/payments/', include('payments.urls')),
]