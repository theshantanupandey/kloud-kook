from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import CustomUser
from .serializers import UserSerializer
from django_otp.plugins.otp_totp.models import TOTPDevice
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class UserCreate(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def enable_two_factor(request):
    user = request.user
    device = user.get_or_create_totp_device()
    device.save()
    return Response({'detail': 'Two-factor authentication enabled.'})