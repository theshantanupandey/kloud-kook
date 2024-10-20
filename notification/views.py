#pip  install firebase-admin
import firebase_admin
from firebase_admin import credentials, messaging
from django.core.mail import send_mail
from twilio.rest import Client

cred = credentials.Certificate('path-to-your-firebase-credentials.json')
firebase_admin.initialize_app(cred)

def send_push_notification(request):
    message = messaging.Message(
        notification=messaging.Notification(
            title='New Order',
            body='You have a new order!',
        ),
        token='device-token',
    )
    response = messaging.send(message)
    return JsonResponse({'response': response})

def send_email_notification(request):
    send_mail(
        'New Order',
        'You have a new order!',
        'from@example.com',
        ['to@example.com'],
        fail_silently=False,
    )
    return JsonResponse({'status': 'Email sent'})

def send_sms_notification(request):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body='You have a new order!',
        from_=TWILIO_PHONE_NUMBER,
        to='+1234567890'
    )
    return JsonResponse({'status': 'SMS sent', 'message_sid': message.sid})