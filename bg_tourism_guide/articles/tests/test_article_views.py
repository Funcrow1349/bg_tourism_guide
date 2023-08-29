from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from bg_tourism_guide.articles.models import Article

CustomUser = get_user_model()

# VALID_ARTICLE_DATA = {
#     'title': 'Some valid title',
#     'body': 'Some valid body',
#     'article_image': 'https://th.bing.com/th/id/OIP.fSo5HMXhsaMA3S8IfAO_CAHaE7?pid=ImgDet&rs=1',
# }
#
# VALID_AUTHOR_DATA = {
#     'first_name': 'Tester',
#     'last_name': 'Testing',
#     'email': 'some_tester@gmail.com',
#     'username': 'Some tester'
# }
#
#
# def _create_article(**kwargs):
#     author = CustomUser.objects.create(**VALID_AUTHOR_DATA)
#     article_data = {
#         **kwargs,
#         'author': author,
#     }
#
#     return Article(**article_data)


class ArticleDetailsViewTests(TestCase):

    def setUp(self):
        self.article = Article.objects.create(
            title='Test Article',
            body='Test body content',
            article_image='https://example.com/test-image.jpg'
        )

    # def test_article_detail_view_get_request_returns_correct_response(self):
    #     article = _create_article(**VALID_ARTICLE_DATA)
    #     article.save()
    #
    #     response = self.client.get(
    #         reverse('article details')
    #     )
    #
    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'articles/article_details.html')

    def test_article_details_view(self):
        url = reverse('article details', args=[self.article.slug])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'articles/article_details.html')
        self.assertContains(response, self.article.title)


class ArticleCreateViewTests(TestCase):
    pass


class ArticleEditViewTests(TestCase):
    pass


class ArticleDeleteViewTests(TestCase):
    pass

