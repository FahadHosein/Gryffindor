from django.test import SimpleTestCase
from django.urls import reverse, resolve
from login.views import sitehome #,redirlogin, redirlogout, info, accounterror, faq, advisories 


class TestUrls(SimpleTestCase):

   def test_sitehome_url_is_resolved(self):
      url = reverse('sitehome')
       print(resolve(url))
       
