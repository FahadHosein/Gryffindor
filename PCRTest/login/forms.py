from django import forms
from django.forms import ModelForm
from .models import appt
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import DateInput

class DateInput(forms.DateInput):
    input_type = 'date'

class AppointmentForm(forms.ModelForm):
    appdate = forms.DateField(widget=DateInput)
    class Meta:
        model=  appt
        fields = [ 'fname', 'lname','cov6','heart','chestpa','phon','emephon','appdate','apptime' ]


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    dob = forms.DateField(widget=DateInput)

    class Meta:
        model = User
        fields = ['username','email','dob','password1','password2']



