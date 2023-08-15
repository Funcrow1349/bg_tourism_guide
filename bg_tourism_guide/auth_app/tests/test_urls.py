from django.test import SimpleTestCase
from django.urls import reverse, resolve

from bg_tourism_guide.auth_app.views import ProfileCreateView, ProfileLoginView, ProfileLogoutView, ProfileEditView, \
    ProfileDeleteView, ProfileDetailsView


class TestAuthUrls(SimpleTestCase):

    def test_create_user_url_resolves(self):
        url = reverse('user create')
        self.assertEquals(resolve(url).func.view_class, ProfileCreateView)

    def test_login_user_url_resolves(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func.view_class, ProfileLoginView)

    def test_logout_user_url_resolves(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func.view_class, ProfileLogoutView)

    def test_edit_user_url_resolves(self):
        user_id = 1
        url = reverse('user edit', args=[user_id])
        self.assertEquals(resolve(url).func.view_class, ProfileEditView)

    def test_delete_user_url_resolves(self):
        user_id = 1
        url = reverse('user delete', args=[user_id])
        self.assertEquals(resolve(url).func.view_class, ProfileDeleteView)

    def test_details_user_url_resolves(self):
        user_id = 1
        url = reverse('user details', args=[user_id])
        self.assertEquals(resolve(url).func.view_class, ProfileDetailsView)
