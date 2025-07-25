from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    is_vendor = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=True)

    def __str__(self):
        return self.username

class VendorProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=100)
    store_description = models.TextField(blank=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.store_name

class CustomerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return f"Customer: {self.user.username}"
