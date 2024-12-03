from django import forms
from django.contrib.auth.models import User
from .models import ShoppingList

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class ShoppingListForm(forms.ModelForm):
    class Meta:
        model = ShoppingList
        fields = ['product_name', 'quantity']