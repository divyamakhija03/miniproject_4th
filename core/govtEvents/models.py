from django.db import models

# Create your models here.
class events(models.Model):
    event_name = models.CharField(max_length=80)
    event_description = models.CharField(max_length=1000)
    event_date = models.DateField()
    event_contact = models.CharField(max_length=50)