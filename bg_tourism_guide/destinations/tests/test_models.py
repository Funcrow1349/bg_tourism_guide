from django.core.exceptions import ValidationError
from django.test import TestCase

from bg_tourism_guide.auth_app.models import CustomUser
from bg_tourism_guide.destinations.models import Destination


class DestinationModelTests(TestCase):
    VALID_DESTINATION_DATA = {
        'name': 'Example Destination',
        'type': 'Beach area',
        'location': 'Some place',
        'destination_image': 'https://th.bing.com/th/id/OIP.fSo5HMXhsaMA3S8IfAO_CAHaE7?pid=ImgDet&rs=1',

    }

    VALID_AUTHOR_DATA = {
        'first_name': 'Tester',
        'last_name': 'Testing',
        'email': 'some_tester@gmail.com',
        'username': 'Some tester'
    }

    def _create_destination(self, data, **kwargs):
        author = CustomUser.objects.create(**self.VALID_AUTHOR_DATA)
        destination_data = {
            **data,
            **kwargs,
            'author': author,
        }

        return Destination(**destination_data)

    def test_create_destination_when_valid_data_expect_to_be_created(self):
        destination = self._create_destination(self.VALID_DESTINATION_DATA)
        destination.full_clean()
        destination.save()

        self.assertIsNotNone(destination.pk)

    def test_create_destination_when_name_max_length_exceeded_expect_to_raise(self):
        destination = self._create_destination(
            self.VALID_DESTINATION_DATA, name='t' * Destination.DESTINATION_NAME_MAX_LENGTH + 't'
        )

        with self.assertRaises(ValidationError):
            destination.full_clean()

    def test_create_destination_when_name_min_length_not_reached_expect_to_raise(self):
        destination = self._create_destination(
            self.VALID_DESTINATION_DATA, name='t' * (Destination.DESTINATION_NAME_MIN_LENGTH - 1)
        )

        with self.assertRaises(ValidationError):
            destination.full_clean()

    def test_create_destination_when_name_starts_with_lower_case_expect_to_raise(self):
        destination = self._create_destination(self.VALID_DESTINATION_DATA, name='some invalid name')

        with self.assertRaises(ValidationError):
            destination.full_clean()

    def test_create_destination_when_location_starts_with_lower_case_expect_to_raise(self):
        destination = self._create_destination(self.VALID_DESTINATION_DATA, location='some invalid location')

        with self.assertRaises(ValidationError):
            destination.full_clean()

    def test_slug_successfully_created(self):
        destination = self._create_destination(self.VALID_DESTINATION_DATA)
        destination.full_clean()
        destination.save()

        self.assertEquals(destination.slug, f'example-destination-{destination.id}')

    def test__str__method_returns_correct_string(self):
        destination = self._create_destination(self.VALID_DESTINATION_DATA)
        destination.full_clean()
        destination.save()

        self.assertEquals(str(destination), destination.name)
