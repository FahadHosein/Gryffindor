from django.urls import path
from . import views
from .views import ApptListView,ApptCreateView
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.sitehome, name='sitehome'),
    path('bookappointment',ApptCreateView.as_view(), name='bookappointment'),
    path('login',auth_views.LoginView.as_view(template_name='login/redirlogin.html'), name='redirlogin'),
    path('logout',auth_views.LogoutView.as_view(template_name='login/redirlogout.html'), name='redirlogout'),
    path('viewresult', ApptListView.as_view(), name='viewresult'),
    path('info/',views.info, name='info'),
    path('accounterror',views.accounterror, name='accounterror'),

]

