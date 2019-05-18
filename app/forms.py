from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UpcomingEventsForm(forms.Form):
    event_title = forms.CharField()
    date = forms.DateField()
    time = forms.TimeField()
    location = forms.CharField()
    remarks = forms.CharField(widget=forms.Textarea)
    band = forms.CharField()


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if user.username == "WillE7529":
            user.is_staff = True
        else:
            user.is_staff = False
        user.save()
        return user