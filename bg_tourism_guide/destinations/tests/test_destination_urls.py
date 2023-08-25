from django.test import SimpleTestCase
from django.urls import reverse, resolve
from bg_tourism_guide.destinations.views import AddDestination, DestinationEditView, DestinationDeleteView, \
    DestinationDetailsView


class TestDestinationUrls(SimpleTestCase):

    def test_add_destination_url_resolves(self):
        url = reverse('add destination')
        self.assertEquals(resolve(url).func.view_class, AddDestination)

    def test_edit_destination_url_resolves(self):
        url = reverse('edit destination', args=['some_slug'])
        self.assertEquals(resolve(url).func.view_class, DestinationEditView)

    def test_delete_destination_url_resolves(self):
        url = reverse('delete destination', args=['some_slug'])
        self.assertEquals(resolve(url).func.view_class, DestinationDeleteView)

    def test_details_destination_url_resolves(self):
        url = reverse('destination details', args=['some_slug'])
        self.assertEquals(resolve(url).func.view_class, DestinationDetailsView)
