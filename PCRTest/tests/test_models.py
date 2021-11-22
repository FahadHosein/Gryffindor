from django.test import TestCase
from login.models import appt

class BasicTest(TestCase):
    def test_first_name_appt(self):
        fname=appt()
        fname.fname = "First Name"
        fname.save()
        
        record = fname.objects.get(pk=fname.id)
        self.assertEqual(record,fname)