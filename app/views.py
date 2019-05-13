from django.shortcuts import render
from django.views import View
from app import forms
from app import models
from django.shortcuts import redirect, render


#view for home page
class HomePage(View):
    def get(self, request):
        return render(request, "home.html")