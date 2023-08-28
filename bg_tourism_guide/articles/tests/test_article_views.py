from django.contrib.auth import get_user_model
from django.test import TestCase, Client

from bg_tourism_guide.articles.models import Article

CustomUser = get_user_model()


class ArticleViewTests(TestCase):
    VALID_ARTICLE_DATA = {
        'title': 'Some valid title',
        'body': 'Some valid body',
        'article_image': 'https://th.bing.com/th/id/OIP.fSo5HMXhsaMA3S8IfAO_CAHaE7?pid=ImgDet&rs=1',
    }

    VALID_AUTHOR_DATA = {
        'first_name': 'Tester',
        'last_name': 'Testing',
        'email': 'some_tester@gmail.com',
        'username': 'Some tester'
    }

    def setUp(self):
        self.test_client = Client()

    def test_article_detail_view_get_request_returns_correct_response(self):
        # self.author = CustomUser.objects.create(**self.VALID_AUTHOR_DATA)
        # self.article = Article.objects.create(**self.VALID_ARTICLE_DATA)
        response = self.test_client.get('article/')

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'articles/article_details.html')
