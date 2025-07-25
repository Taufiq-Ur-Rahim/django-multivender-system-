from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser, VendorProfile, CustomerProfile

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_vendor:
            VendorProfile.objects.create(user=instance)
        else:
            CustomerProfile.objects.create(user=instance)
