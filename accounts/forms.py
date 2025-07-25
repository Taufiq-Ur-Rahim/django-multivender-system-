from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, VendorProfile

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'is_vendor')

class VendorProfileForm(forms.ModelForm):
    class Meta:
        model = VendorProfile
        fields = ['store_name', 'store_description']
