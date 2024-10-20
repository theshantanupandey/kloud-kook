from rest_framework import generics
from .models import Delivery
from .serializers import DeliverySerializer
import googlemaps
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response

class DeliveryListCreate(generics.ListCreateAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer

class DeliveryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer


gmaps = googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY)

@api_view(['POST'])
def optimize_route(request):
    origin = request.data.get('origin')
    destinations = request.data.get('destinations')

    directions_result = gmaps.directions(origin, destinations, mode="driving")
    return Response(directions_result)

@api_view(['POST'])
def track_delivery(request):
    delivery_id = request.data.get('delivery_id')
    delivery = Delivery.objects.get(id=delivery_id)
    location = gmaps.geocode(delivery.order.user.address)
    return Response(location)