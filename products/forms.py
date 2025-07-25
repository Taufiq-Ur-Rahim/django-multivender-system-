from django import forms

from .models import Product, ProductImage

class ProductForm(forms.ModelForm):
    # To support multiple images, handle request.FILES.getlist('images') in your view
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock', 'category']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Enter product name'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control', 'rows': 4, 'placeholder': 'Enter product description'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control', 'placeholder': 'Enter product price'
            }),
            'stock': forms.NumberInput(attrs={
                'class': 'form-control', 'placeholder': 'Enter available stock'
            }),
            'category': forms.Select(attrs={
                'class': 'form-select'
            }),
        }
