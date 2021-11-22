from django.test import TestCase

from login.forms import UserRegistrationForm

class TestUserRegistrationform(TestCase):
    """
    TESTS: form.is_valid
    """
    # form.is_valid=True

    def test_form_valid_middle_optional_blank(self):
        name_form_data = {'username': 'Duane',     # Required
                            'email': 'duane@gmail.com',       # Required
                            'dob': '12-1-2021',     # Required
                            'password1': '12345', # Required
                            'password2': '12364', # Required
                        }
        name_form = UserRegistrationForm(data=name_form_data)