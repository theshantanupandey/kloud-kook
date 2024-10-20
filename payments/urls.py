from django.urls import path
from .views import PaymentListCreate, PaymentDetail, BillingListCreate, BillingDetail

urlpatterns = [
    path('payments/', PaymentListCreate.as_view(), name='payment-list-create'),
    path('payments/<int:pk>/', PaymentDetail.as_view(), name='payment-detail'),
    path('billing/', BillingListCreate.as_view(), name='billing-list-create'),
    path('billing/<int:pk>/', BillingDetail.as_view(), name='billing-detail'),
    path('create-customer/', create_customer, name='create-customer'),
    path('create-charge/', create_charge, name='create-charge'),
    path('sync-with-xero/', sync_with_xero, name='sync-with-xero')
]