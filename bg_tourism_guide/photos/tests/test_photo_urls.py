from django.test import SimpleTestCase
from django.urls import reverse, resolve

from bg_tourism_guide.photos.views import AddPhoto, DeletePhoto, photo_page


class TestPhotoUrls(SimpleTestCase):

    def test_add_photo_url_resolves(self):
        url = reverse('add photo')
        self.assertEquals(resolve(url).func.view_class, AddPhoto)

    def test_delete_photo_url_resolves(self):
        photo_id = 1
        url = reverse('delete photo', args=[photo_id])
        self.assertEquals(resolve(url).func.view_class, DeletePhoto)

    def test_details_photo_url_resolves(self):
        photo_id = 1
        url = reverse('photo page', args=[photo_id])
        self.assertEquals(resolve(url).func, photo_page)
