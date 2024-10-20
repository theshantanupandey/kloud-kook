from django.contrib.auth.models import Group, Permission
from django.db import models
from django_otp.plugins.otp_totp.models import TOTPDevice
from auditlog.registry import auditlog

class CustomUser(AbstractUser):
    # Existing fields
    role = models.CharField(max_length=50, choices=[('customer', 'Customer'), ('staff', 'Staff')], default='customer')
    auditlog.register(CustomUser)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.role == 'staff':
            staff_group, created = Group.objects.get_or_create(name='Staff')
            self.groups.add(staff_group)
        elif self.role == 'customer':
            customer_group, created = Group.objects.get_or_create(name='Customer')
            self.groups.add(customer_group)

    def get_or_create_totp_device(self):
        device, created = TOTPDevice.objects.get_or_create(user=self, name='default')
        return device
    
class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    preferences = models.JSONField(default=dict)

    def __str__(self):
        return self.user.username
    

