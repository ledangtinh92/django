from django import forms

from apps.myapp.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'stock' , 'category', 'description']
