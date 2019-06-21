from django.db import models
from datetime import datetime, timedelta

# Create your models here.
class ShowsManager(models.Manager):
    def validate(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors["title"] = "Title should be at least 2 characters long."
        if len(postData['network']) < 3:
            errors["network"] = "Network should be at least 3 characters."
        if len(postData['description']) != 0 and len(postData['description']) < 10:
            errors["description"] = "Description is optional but should be at least 10 characters if provided."
        release_dt = datetime.strptime(postData['release_date'], "%Y-%m-%d")
        if release_dt > datetime.now():
            errors['date'] = "Release date must be in the past"
        if len(self.filter(title=postData['title'])) > 0 :
            errors['dup'] = "Title must be unique!"
        return errors



class Trips(models.Model):
    destination = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    trip_start = models.DateField()
    trip_end = models.DateFiedl()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    uploaded_by = models.ForeignKey(User, related_name="books_uploaded")
    users_who_like = models.ManyToManyField(User, related_name="liked_books")
    objects = ShowsManager()

