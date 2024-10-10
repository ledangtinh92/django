from django import forms

from apps.myapp.models import ProductCategory

class ProductCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ['name', 'color']