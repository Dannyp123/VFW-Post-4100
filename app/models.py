from django.db import models


# Create your models here.
class UpcomingEvents(models.Model):
    event_title = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    band = models.TextField()
    remarks = models.TextField()
    location = models.TextField()

    @staticmethod
    def submit_events(event_title, date, time, band, remarks, location):
        UpcomingEvents(
            event_title=event_title,
            date=date,
            time=time,
            band=band,
            remarks=remarks,
            location=location).save()
