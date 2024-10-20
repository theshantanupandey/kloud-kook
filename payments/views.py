from rest_framework import generics
from .models import Payment, Billing
from .serializers import PaymentSerializer, BillingSerializer
from xero import Xero
from xero.auth import PrivateCredentials

class PaymentListCreate(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class PaymentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class BillingListCreate(generics.ListCreateAPIView):
    queryset = Billing.objects.all()
    serializer_class = BillingSerializer

class BillingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Billing.objects.all()
    serializer_class = BillingSerializer


def sync_with_xero(request):
    with open(XERO_PRIVATE_KEY_PATH) as keyfile:
        rsa_key = keyfile.read()
    credentials = PrivateCredentials(XERO_CONSUMER_KEY, rsa_key)
    xero = Xero(credentials)
    invoices = xero.invoices.filter(Status='AUTHORISED')
    return JsonResponse({'invoices': invoices})