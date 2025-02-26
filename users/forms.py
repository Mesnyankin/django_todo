from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите имя пользователя', 'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль', 'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Подтвердите пароль', 'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']