from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import appt


   
def home(request):
    form = UserCreationForm()
    return render(request, 'login/homelogin.html', {'form' : form})

def bookappointment(request):
    context = {
    'appt':appt.objects.all()
    } 
    return render(request, 'login/bookappointment.html', context)

def viewresult(request):
    context = {
    'appt':appt.objects.all()
    } 
    return render(request, 'login/viewresult.html', context)

def info(request):
    return render(request, 'login/infopage.html')