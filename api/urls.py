from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet, OrderViewSet, MealViewSet, IngredientViewSet, SupplierViewSet,
    DeliveryViewSet, PaymentViewSet, BillingViewSet, MessageViewSet, TaskViewSet
)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'meals', MealViewSet)
router.register(r'ingredients', IngredientViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'deliveries', DeliveryViewSet)
router.register(r'payments', PaymentViewSet)
router.register(r'billing', BillingViewSet)
router.register(r'messages', MessageViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('v1/', include((router.urls, 'api'), namespace='v1')),
     path('search/', search, name='search'),
]