from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class appt(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=40)
    cov6 = models.BooleanField(null=True)
    heart = models.BooleanField(null=True)
    chestpa = models.BooleanField(null=True)
    phon = models.IntegerField(null=True)
    emephon = models.IntegerField(null=True)
    #email = models.EmailField(null=True ,max_length=254)
    appdatetime = models.DateTimeField(default=timezone.now)    
    test = models.BooleanField(null=True)

    