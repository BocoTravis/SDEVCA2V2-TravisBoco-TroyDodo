from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'price', 'sale_price', 'on_sale', 'image', 'stock', 'available', 'is_popular']
