from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import CustomUserCreationForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("task_list")
        else:
            messages.error(request, "Registration error. Check the entered data.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})