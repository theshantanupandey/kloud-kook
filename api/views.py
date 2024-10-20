from rest_framework import viewsets
from users.models import CustomUser
from users.serializers import UserSerializer
from orders.models import Order
from orders.serializers import OrderSerializer
from meals.models import Meal
from meals.serializers import MealSerializer
from inventory.models import Ingredient, Supplier
from inventory.serializers import IngredientSerializer, SupplierSerializer
from delivery.models import Delivery
from delivery.serializers import DeliverySerializer
from payments.models import Payment, Billing
from payments.serializers import PaymentSerializer, BillingSerializer
from communication.models import Message, Task
from communication.serializers import MessageSerializer, TaskSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework_api_key.permissions import HasAPIKey
from haystack.query import SearchQuerySet
from rest_framework.decorators import api_view
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['username', 'email', 'role']

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'status', 'created_at', 'updated_at']

class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class DeliveryViewSet(viewsets.ModelViewSet):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class BillingViewSet(viewsets.ModelViewSet):
    queryset = Billing.objects.all()
    serializer_class = BillingSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwnerOrReadOnly]

@api_view(['GET'])
def search(request):
    query = request.GET.get('q', '')
    results = SearchQuerySet().filter(content=query)
    return Response({'results': [result.object for result in results]})