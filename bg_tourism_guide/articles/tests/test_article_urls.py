from django.test import SimpleTestCase
from django.urls import reverse, resolve

from bg_tourism_guide.articles.views import AddArticle, ArticleEditView, ArticleDeleteView, ArticleDetailsView


class TestArticleUrls(SimpleTestCase):

    def test_add_article_url_resolves(self):
        url = reverse('add article')
        self.assertEquals(resolve(url).func.view_class, AddArticle)

    def test_edit_article_url_resolves(self):
        url = reverse('edit article', args=['some_slug'])
        self.assertEquals(resolve(url).func.view_class, ArticleEditView)

    def test_delete_article_url_resolves(self):
        url = reverse('delete article', args=['some_slug'])
        self.assertEquals(resolve(url).func.view_class, ArticleDeleteView)

    def test_details_article_url_resolves(self):
        url = reverse('article details', args=['some_slug'])
        self.assertEquals(resolve(url).func.view_class, ArticleDetailsView)
