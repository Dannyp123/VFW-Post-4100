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
        return render(request, "home.html")


class MakeEvents(View):
    def get(self, request):
        return render(request, "events-form.html",
                      {"events_form": forms.UpcomingEventsForm()})

    def post(self, request):
        form = forms.UpcomingEventsForm(data=request.POST)
        if form.is_valid():
            event_title = form.cleaned_data["event_title"]
            date = form.cleaned_data["date"]
            time = form.cleaned_data["time"]
            band = form.cleaned_data["band"]

            models.UpcomingEvents.submit_events(event_title, date, time, band)

            return redirect("home")
        else:
            return render(request, "events-form.html", {"events_form": form})


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Welcome!")
            return redirect("login")
    else:
        form = UserRegisterForm()

    return render(request, "sign-up.html", {"form": form})


@login_required
def profile(request):
    return render(request, "profile.html")