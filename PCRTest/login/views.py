from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UserRegistrationForm
from .models import appt
from django.contrib import messages

   
def sitehome(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username') 
            messages.success(request, f'Account creation for {username} succesful!')
            return redirect('viewresult')
    else:
        form = UserRegistrationForm() 
    return render(request, 'login/homesignup.html', {'form' : form})

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


def redirlogin(request):
    return render(request, 'login/redirlogin.html')    

def info(request):
    return render(request, 'login/infopage.html')