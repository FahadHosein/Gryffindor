from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.utils import timezone


class appt(models.Model):
    
    fname = models.CharField("First Name",max_length=20)
    lname = models.CharField("Last Name",max_length=40)
    cov6 = models.BooleanField("Did you have Covid-19 in the past 6 months ?",null=True)
    heart = models.BooleanField("Do you have regular heart problems ?",null=True)
    chestpa = models.BooleanField("Do you have regular chest pains ?",null=True)
    phon = models.IntegerField("Personal Phone Number",null=True)
    emephon = models.IntegerField("Emergency Contact number",null=True)
    appdate = models.DateField("Appointment Date",default=timezone.now)   
    apptime = models.TimeField("Appointment Time",default=timezone.now)   
    apprequest = models.BooleanField(null=True)
    appconfirmed = models.BooleanField(null=True)
    tested = models.BooleanField(null=True)
    result = models.BooleanField(null=True)
    requesttime = models.DateTimeField("Request Date/Time",default=timezone.now)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return  self.fname + ' ' + self.lname 
   
  
    