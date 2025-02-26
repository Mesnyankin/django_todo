from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.forms import DateInput
from .models import Task

class TaskForm(forms.ModelForm):
    due_date = forms.DateField(widget=DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Task
        fields = ["title", "description", "due_date", "completed"]
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Введите заголовок'}),
            'description': forms.Textarea(attrs={'placeholder': 'Введите описание задачи'}),
        }

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите имя пользователя', 'autocomplete': 'off'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль', 'autocomplete': 'off'}))