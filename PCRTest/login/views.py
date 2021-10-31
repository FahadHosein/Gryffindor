from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import ListView,CreateView
from .forms import UserRegistrationForm
from .models import appt
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

   
def sitehome(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username') 
            messages.success(request, f'Account creation for {username} succesful!')
            return redirect('redirlogin')
    else:
        form = UserRegistrationForm() 
    return render(request, 'login/homesignup.html', {'form' : form})



@method_decorator(login_required, name='dispatch')
class ApptListView(ListView):
    model = appt
    template_name = 'login/viewresult.html'
    context_object_name = 'appt'




@method_decorator(login_required, name='dispatch')
class ApptCreateView(CreateView):
    model = appt
    fields = [ 'fname', 'lname','cov6','heart','chestpa','phon','emephon','appdatetime']
    template_name = 'login/bookappointment.html'
    success_url = 'viewresult'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)




def redirlogin(request):
    return render(request, 'login/redirlogin.html')    

def redirlogout(request):
    return render(request, 'login/redirlogout.html')    

def info(request):
    return render(request, 'login/infopage.html')

def accounterror(request):
    return render(request, 'login/accounterror.html')  

def faq(request):
    return render(request, 'login/faq.html')  

def advisories(request):
    return render(request, 'login/covidadvisories.html')  