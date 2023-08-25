from django.core.exceptions import ValidationError
from django.test import TestCase
from bg_tourism_guide.auth_app.models import CustomUser


class UserModelTests(TestCase):

    VALID_USER_DATA = {
        'first_name': 'Ivan',
        'last_name': 'Ivanov',
        'username': 'TestName',
        'email': 'test@email.com',
    }

    def _create_user(self, data, **kwargs):
        user = CustomUser.objects.create(**self.VALID_USER_DATA)
        return user

    def test_create_user_when_data_is_valid_expect_to_create(self):
        user = self._create_user(self.VALID_USER_DATA)
        self.assertIsNotNone(user.id)

    def test_create_user_when_first_name_starts_with_lowercase_expect_to_raise(self):
        user = self._create_user(self.VALID_USER_DATA, first_name='ivan')

        with self.assertRaises(ValidationError):
            user.full_clean()

    def test_create_user_when_first_name_contains_invalid_chars_expect_to_raise(self):
        user = self._create_user(self.VALID_USER_DATA, first_name='Vank0')

        with self.assertRaises(ValidationError):
            user.full_clean()

    def test_create_user_when_last_name_starts_with_lowercase_expect_to_raise(self):
        user = self._create_user(self.VALID_USER_DATA, last_name='ivanov')

        with self.assertRaises(ValidationError):
            user.full_clean()

    def test_create_user_when_last_name_contains_invalid_chars_expect_to_raise(self):
        user = self._create_user(self.VALID_USER_DATA, last_name='Ivan0v')

        with self.assertRaises(ValidationError):
            user.full_clean()

    def test_create_user_when_username_starts_with_lowercase_expect_to_raise(self):
        user = self._create_user(self.VALID_USER_DATA, username='tester')

        with self.assertRaises(ValidationError):
            user.full_clean()

    def test__str__method_return_correct_string(self):
        user = self._create_user(self.VALID_USER_DATA)

        self.assertEquals(str(user), f"{user.first_name} {user.last_name}")

