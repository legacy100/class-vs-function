from django.db import models
from django import forms
from .models import *

class ProductForm(forms.ModelForm):

    class Meta:
        model = Products
        fields = '__all__'
        # ('name','price','stock','image_url')

        # widgets = {
        #     'name': forms.TextInput(attrs={'class':'form-control'}),
        #     'price': forms.TextInput(attrs={'class':'form-control'}),
        #     'stock': forms.TextInput(attrs={'class':'form-control'}),
        #     'image_url':forms.ClearableFileInput(attrs={'type':'image_url'}),
        # }


        