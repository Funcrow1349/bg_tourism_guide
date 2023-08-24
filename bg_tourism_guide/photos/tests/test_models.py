from django.core.exceptions import ValidationError
from django.test import TestCase

from bg_tourism_guide.auth_app.models import CustomUser
from bg_tourism_guide.photos.models import Photo


class PhotoModelTests(TestCase):
    VALID_PHOTO_DATA = {
        'photo': 'https://th.bing.com/th/id/OIP.fSo5HMXhsaMA3S8IfAO_CAHaE7?pid=ImgDet&rs=1',
        'description': 'A very nice photo indeed',
        'location': 'Test, Bulgaria'
    }

    VALID_AUTHOR_DATA = {
        'first_name': 'Tester',
        'last_name': 'Testing',
        'email': 'some_tester@gmail.com',
        'username': 'Some tester'
    }

    def _create_photo(self, data, **kwargs):
        author = CustomUser.objects.create(**self.VALID_AUTHOR_DATA)
        article_data = {
            **data,
            **kwargs,
            'uploaded_by': author,
        }

        return Photo(**article_data)

    def test_create_photo_when_valid_data_expect_to_be_created(self):
        photo = self._create_photo(self.VALID_PHOTO_DATA)
        photo.full_clean()
        photo.save()

        self.assertIsNotNone(photo.pk)

    def test_create_photo_when_description_max_length_exceeded_expect_to_raise(self):
        photo = self._create_photo(self.VALID_PHOTO_DATA, description='t' * Photo.DESCRIPTION_MAX_LENGTH + 't')

        with self.assertRaises(ValidationError):
            photo.full_clean()

    def test_create_photo_when_description_min_length_not_reached_expect_to_raise(self):
        photo = self._create_photo(self.VALID_PHOTO_DATA, description='t' * (Photo.DESCRIPTION_MIN_LENGTH - 1))

        with self.assertRaises(ValidationError):
            photo.full_clean()

    def test_create_photo_when_description_starts_with_lowercase_expect_to_raise(self):
        photo = self._create_photo(self.VALID_PHOTO_DATA, description='example')

        with self.assertRaises(ValidationError):
            photo.full_clean()

    def test_create_photo_when_location_starts_with_lowercase_expect_to_raise(self):
        photo = self._create_photo(self.VALID_PHOTO_DATA, location='example')

        with self.assertRaises(ValidationError):
            photo.full_clean()

    def test__str__method_returns_correct_string(self):
        photo = self._create_photo(self.VALID_PHOTO_DATA)
        photo.full_clean()
        photo.save()

        self.assertEquals(str(photo), 'A very nice photo indeed')
