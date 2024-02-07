from django.db import models

from account.models import User

# Create your models here.

class Gri(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=15)
    address = models.TextField()
    grievance_category = models.CharField(max_length=50)
    other_category = models.CharField(max_length=50, blank=True)
    grievance_description = models.TextField()
    attachment = models.FileField(upload_to='attachments/', blank=True)
    preferred_resolution = models.CharField(max_length=20)
    submit_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Gri #{self.id}"