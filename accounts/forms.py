from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, VendorProfile

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'is_vendor')

    def save(self, commit=True):
        user = super().save(commit=False)
        # If is_vendor is checked, set is_customer to False
        if self.cleaned_data.get('is_vendor'):
            user.is_customer = False
        else:
            user.is_customer = True
        if commit:
            user.save()
        return user

class VendorProfileForm(forms.ModelForm):
    class Meta:
        model = VendorProfile
        fields = ['store_name', 'store_description']
