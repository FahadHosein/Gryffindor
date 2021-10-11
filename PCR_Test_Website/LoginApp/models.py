# Defining Model classes for the app to pull out data from the database

from django.db import models
from django.db.models.expressions import F

# Create your models here.

# General User Model 
class General_User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dob = models.DateField(null=False)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)


# Staff User Model 



# Admin User Model 