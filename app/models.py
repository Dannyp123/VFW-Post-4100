from django.db import models


# Create your models here.
class UpcomingEvents(models.Model):
    event_title = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    band = models.TextField()

    @staticmethod
    def submit_events(event_title, date, time, band):
        UpcomingEvents(
            event_title=event_title, date=date, time=time, band=band).save()
