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
            event_title = form.cleaned_data.get("event_title")
            date = form.cleaned_data.get("date")
            time = form.cleaned_data.get("time")
            band = form.cleaned_data.get("band")
            remarks = form.cleaned_data.get("remarks")
            location = form.cleaned_data.get("location")

            models.UpcomingEvents.submit_events(event_title, date, time, band,
                                                remarks, location)

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


class allUpcomingEvents(View):
    def get(self, request):
        return render(
            request, "all-events.html",
            {"events": models.UpcomingEvents.objects.all().order_by("date")})


class UpcomingEvent(View):
    def get(self, request, id):
        return render(request, "event.html",
                      {"event": models.UpcomingEvents.objects.get(id=id)})


class DeleteEvent(View):
    def get(self, request, id):
        models.UpcomingEvents.objects.get(id=id).delete()
        return redirect("all-events")


@login_required
def profile(request):
    return render(request, "profile.html")