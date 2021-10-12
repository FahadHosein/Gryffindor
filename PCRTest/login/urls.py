from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='sitehome'),
    path('bookappointment',views.bookappointment, name='bookappointment'),
    path('viewresult',views.viewresult, name='viewresult'),
    path('info/',views.info, name='info'),

]

