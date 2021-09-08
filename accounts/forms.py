from .models import CustomUser
from django import forms 
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username','email','age',)
class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomUser
        fields = ('username','email','age',)
