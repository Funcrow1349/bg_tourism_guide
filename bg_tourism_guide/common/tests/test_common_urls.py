from django.test import SimpleTestCase
from django.urls import reverse, resolve

from bg_tourism_guide.common.views import index_view, gallery_view, destinations_view, articles_view


class TestCommonUrls(SimpleTestCase):

    def test_index_url_resolves(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index_view)

    def test_browse_gallery_url_resolves(self):
        url = reverse('browse gallery')
        self.assertEquals(resolve(url).func, gallery_view)

    def test_browse_destinations_url_resolves(self):
        url = reverse('browse destinations')
        self.assertEquals(resolve(url).func, destinations_view)

    def test_browse_articles_url_resolves(self):
        url = reverse('browse articles')
        self.assertEquals(resolve(url).func, articles_view)
