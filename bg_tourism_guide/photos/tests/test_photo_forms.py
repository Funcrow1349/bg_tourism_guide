from django.test import TestCase

from bg_tourism_guide.photos.forms import PhotoCreateForm


class PhotoFormTests(TestCase):

    def test_create_photo_when_form_data_is_valid(self):
        data = {
            'photo': 'https://th.bing.com/th/id/OIP.fSo5HMXhsaMA3S8IfAO_CAHaE7?pid=ImgDet&rs=1',
            'description': 'Some random description',
            'location': 'Sofia, Bulgaria',
        }

        form = PhotoCreateForm(data)
        self.assertTrue(form.is_valid())

    def test_create_photo_when_form_data_is_invalid_expect_to_raise(self):
        data = {
            'photo': 'https://th.bing.com/th/id/OIP.fSo5HMXhsaMA3S8IfAO_CAHaE7?pid=ImgDet&rs=1',
            'description': 'some random description',
            'location': 'sofia, Bulgaria',
        }

        form = PhotoCreateForm(data)
        self.assertFalse(form.is_valid())
