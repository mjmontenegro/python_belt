from django.db import models
from apps.Login_Reg_App.models import User
from datetime import datetime

# Create your models here.
class TripManager(models.Manager):
    def trip_validator(self,postData):
        errors = {}
        if len(postData['destination']) < 3:
            errors["destination"] = "The destination is required and must be at least 3 characters long"
        if len(postData['plan']) < 3:
            errors["plan"] = "A plan is required and must be at least 3 characters long"
        if len(postData['start_date']) < 1 or len(postData['end_date']) < 1:
            errors["missing_date"] = "A starting and ending date are both required"
        else:
            start_dt = datetime.strptime(postData['start_date'], "%Y-%m-%d")
            end_dt = datetime.strptime(postData['end_date'], "%Y-%m-%d")
            if start_dt < datetime.now():
                errors['past_date'] = "Start dates must be in the future"
            if end_dt < start_dt:
                errors['time_travel'] = "Time travel is not allowed!!!"
        return errors        


class Trip(models.Model):
    destination = models.CharField(max_length=255)
    plan = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    creator = models.ForeignKey(User, related_name="trips_created")
    users_who_joined = models.ManyToManyField(User, related_name="trips_joined")
    objects = TripManager()

