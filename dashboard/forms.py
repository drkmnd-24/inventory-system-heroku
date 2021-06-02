from django import forms
from .models import *


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'quantity']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product','order_qty']
