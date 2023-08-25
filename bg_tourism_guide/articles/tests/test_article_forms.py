from django.test import TestCase

from bg_tourism_guide.articles.forms import ArticleForm


class ArticleFormTests(TestCase):

    def test_create_article_when_form_data_is_valid(self):
        data = {
            'title': 'Some valid title',
            'body': 'Some text',
            'article_image': 'https://th.bing.com/th/id/OIP.fSo5HMXhsaMA3S8IfAO_CAHaE7?pid=ImgDet&rs=1'
        }

        form = ArticleForm(data)
        self.assertTrue(form.is_valid())

    def test_create_article_when_form_data_is_not_valid(self):
        data = {
            'title': 'some invalid title',
            'body': 'Some text',
            'article_image': 'https://th.bing.com/th/id/OIP.fSo5HMXhsaMA3S8IfAO_CAHaE7?pid=ImgDet&rs=1'
        }

        form = ArticleForm(data)
        self.assertFalse(form.is_valid())
