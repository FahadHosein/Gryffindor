from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class appt(models.Model):
    
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=40)
    cov6 = models.BooleanField(null=True)
    heart = models.BooleanField(null=True)
    chestpa = models.BooleanField(null=True)
    phon = models.IntegerField(null=True)
    emephon = models.IntegerField(null=True)
    appdatetime = models.DateTimeField(default=timezone.now)    
    test = models.BooleanField(null=True)
    covnow = models.BooleanField(null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.appdatetime


    def get_absolute_url(self):

        return reverse('apptdetail', kwargs={'pk': self.pk})
    