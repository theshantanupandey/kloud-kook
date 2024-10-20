from django.urls import path
from .views import send_push_notification

urlpatterns = [
    path('send-push-notification/', send_push_notification, name='send-push-notification'),
    path('send-email-notification/', send_email_notification, name='send-email-notification'),
    path('send-sms-notification/', send_sms_notification, name='send-sms-notification'),
]