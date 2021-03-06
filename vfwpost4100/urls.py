"""vfwpost4100 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage.as_view(), name="home"),
    path("signup/", views.register, name="sign-up"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="login.html"),
        name="login"),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="logout.html"),
        name="logout"),
    path("adding-events/", views.MakeEvents.as_view(), name="events"),
    path("profile/", views.profile, name="profile"),
    path(
        "upcoming-events/",
        views.allUpcomingEvents.as_view(),
        name="all-events"),
    path("event/<id>/", views.UpcomingEvent.as_view(), name="event"),
    path(
        "delete-event/<id>/", views.DeleteEvent.as_view(),
        name="delete-event"),
]
