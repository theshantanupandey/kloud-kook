from rest_framework import serializers
from .models import Payment, Billing

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('id', 'order', 'user', 'amount', 'status', 'created_at', 'updated_at')

class BillingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Billing
        fields = ('id', 'user', 'amount', 'description', 'created_at')