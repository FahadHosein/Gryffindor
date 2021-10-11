# Defines the view functions
# A view function takes a request and returns a response
# -- Request Handler

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
 # things we can do 
    # - Pull data from database
    # - Transform data
    # - send emails 

x = 1


def login_page(request):
    ty=4
    z=66
    return render(request,'LoginPage.html',{'Proof1':x,'Proof2':ty,'Proof3':z})

def about_page(request):
    return render(request,'AboutPage.html')