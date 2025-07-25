from django.contrib import admin
from .models import CustomUser,CustomerProfile,VendorProfile
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(VendorProfile)
admin.site.register(CustomerProfile)