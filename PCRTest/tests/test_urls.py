from django.test import SimpleTestCase
from django.urls import reverse, resolve
from login.views import ApptListView,ApptCreateView, sitehome, info, accounterror, faq, advisories
from django.contrib.auth.views import LoginView, LogoutView

class TestLoginUrls(SimpleTestCase):
      
    def test_sitehome_url_is_resolved(self):
        url = reverse('sitehome')
        self.assertEquals(resolve(url).func, sitehome)
    
    def test_result_url_is_resolved(self):
        url = reverse('viewresult')
        self.assertEquals(resolve(url).func.view_class, ApptListView)
        
    def test_login_url_is_resolved(self):
        url = reverse('redirlogin')
        self.assertEquals(resolve(url).func.view_class, LoginView)
        
    def test_logout_url_is_resolved(self):
        url = reverse('redirlogout')
        self.assertEquals(resolve(url).func.view_class, LogoutView)

    def test_bookappointment_url_is_resolved(self):
        url = reverse('bookappointment')
        self.assertEquals(resolve(url).func.view_class, ApptCreateView)
        
    def test_info_url_is_resolved(self):
        url = reverse('info')
        self.assertEquals(resolve(url).func, info)
        
    def test_account_error_url_is_resolved(self):
        url = reverse('accounterror')
        self.assertEquals(resolve(url).func, accounterror)
        
    def test_faq_url_is_resolved(self):
        url = reverse('faq_t')
        self.assertEquals(resolve(url).func, faq)
        
    def test_advisories_url_is_resolved(self):
        url = reverse('covidadvisory')
        self.assertEquals(resolve(url).func, advisories)