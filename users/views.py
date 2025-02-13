from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")  # Перенаправление на страницу входа
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})