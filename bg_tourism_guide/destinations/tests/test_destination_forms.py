from django.test import TestCase

from bg_tourism_guide.destinations.forms import DestinationForm


class DestinationFormTests(TestCase):

    def test_create_destination_when_form_data_is_valid(self):
        data = {
            'name': 'Test Destination',
            'type': 'Natural Site',
            'location': 'Sofia, Bulgaria',
            'destination_image': 'https://th.bing.com/th/id/OIP.fSo5HMXhsaMA3S8IfAO_CAHaE7?pid=ImgDet&rs=1',
        }

        form = DestinationForm(data)
        self.assertTrue(form.is_valid())

    def test_create_destination_when_form_data_is_invalid_expect_to_raise(self):
        data = {
            'name': 'test Destination',
            'type': 'Natural Site',
            'location': 'Sofia, Bulgaria',
            'destination_image': 'https://th.bing.com/th/id/OIP.fSo5HMXhsaMA3S8IfAO_CAHaE7?pid=ImgDet&rs=1',
        }

        form = DestinationForm(data)
        self.assertFalse(form.is_valid())
