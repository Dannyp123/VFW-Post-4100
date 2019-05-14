from django.shortcuts import render
from django.views import View
from app import forms
from app import models
from django.shortcuts import redirect, render
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


#view for home page
class HomePage(View):
    def get(self, request):
        messages.success(request, f"Welcome!")
        return render(request, "home.html")


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request, f"Your account has been created. You can now login")
            return redirect("login")
    else:
        form = UserRegisterForm()

    return render(request, "sign-up.html", {"form": form})