# This module maps the URLs of the browser to our view functions

from django.urls import path
from . import views

# URL configuration
urlpatterns = [
    path('loginuser/',views.login_page,name="Login"),
    path('loginabout',views.about_page,name="About"),

]