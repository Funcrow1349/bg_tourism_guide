from django.test import TestCase
from bg_tourism_guide.auth_app.forms import CustomUserCreationForm


class UserFormTests(TestCase):
    VALID_USER_DATA = {
        'first_name': 'Ivan',
        'last_name': 'Ivanov',
        'username': 'TestName',
        'email': 'test@email.com',
        'password1': 'klls2asdljgRrT',
        'password2': 'klls2asdljgRrT',
    }

    INVALID_USER_DATA = {
        'first_name': 'ivan',
        'last_name': 'Ivanov',
        'username': 'TestName',
        'email': 'test@email.com',
        'password1': 'klls2asdljgRrT',
        'password2': 'klls2asdljgRrT',
    }

    def test_create_user_when_form_data_is_valid(self):

        form = CustomUserCreationForm(self.VALID_USER_DATA)
        self.assertTrue(form.is_valid())

    def test_create_user_when_form_data_is_invalid_expect_to_raise(self):

        form = CustomUserCreationForm(self.INVALID_USER_DATA)
        self.assertFalse(form.is_valid())
