from django.db import models
from datetime import datetime
import re


EMAIL_REGEX = re.compile('^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
DAYS_IN_YEAR = 365


class UserManager(models.Manager):
    def validate_reg(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['fist_name'] = "First name must be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name must be at least 2 characters"
        if not self.valid_email(postData['email']):
            errors['email'] = "Invalid email address"
        elif self.email_in_use(postData['email']):
                errors['email'] = "Email address already in use"
        if not self.valid_password_length(postData['password']):
            errors['password_length'] = "Password must be at least 8 characters"
        if postData['password'] != postData['password_confirm']:
            errors['password_match'] = "Passwords must match"
        if len(postData['birthdate']) == 0:
            errors['birthdate'] = "Birthdate field is required"
        else:
            days_old  = (datetime.now() - datetime.strptime(postData['birthdate'],"%Y-%m-%d")).days
            years_old = days_old / DAYS_IN_YEAR
            if years_old < 0:
                errors['birthdate'] = "Birthdate must be in the past"
            elif years_old < 13:
                errors['age'] = "This website is only for users 13 years or older"
        return errors
    def validate_login(self, postData):
        errors = {}
        if not self.valid_email(postData['email']):
            errors['email'] = "Invalid email address"
        if not self.valid_password_length(postData['password']):
            errors['password_length'] = "Password must be at least 8 characters"
        return errors
    def email_in_use(self, email):
        if len(self.filter(email=email)) == 0:
            return False
        return True
    def valid_email(self, email):
        if not EMAIL_REGEX.match(email):
            return False
        return True
    def valid_password_length(self, password):
        if len(password) < 8:
            return False
        return True


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=100)
    password_hash = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    birthdate = models.DateField(null=True)
    objects = UserManager()


