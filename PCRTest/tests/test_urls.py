
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from login.views import sitehome 


class TestUrls(SimpleTestCase):
   
 def test_sitehome_url_is_resolved(self):
       url = reverse('sitehome')
       self.assertEquals(resolve(url).func, sitehome)
       