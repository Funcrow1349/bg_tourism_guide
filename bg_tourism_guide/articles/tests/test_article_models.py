from django.core.exceptions import ValidationError
from django.test import TestCase

from bg_tourism_guide.articles.models import Article, CustomUser


class ArticleModelTests(TestCase):
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

    def _create_article(self, data, **kwargs):
        author = CustomUser.objects.create(**self.VALID_AUTHOR_DATA)
        article_data = {
            **data,
            **kwargs,
            'author': author,
        }

        return Article(**article_data)

    def test_create_article_when_valid_data_expect_to_be_created(self):
        article = self._create_article(self.VALID_ARTICLE_DATA)
        article.full_clean()
        article.save()

        self.assertIsNotNone(article.pk)

    def test_create_article_when_title_max_length_exceeded_expect_to_raise(self):
        article = self._create_article(self.VALID_ARTICLE_DATA, title='t' * Article.TITLE_MAX_LENGTH + 't')

        with self.assertRaises(ValidationError):
            article.full_clean()

    def test_create_article_when_title_min_length_not_reached_expect_to_raise(self):
        article = self._create_article(self.VALID_ARTICLE_DATA, title='t' * (Article.TITLE_MIN_LENGTH - 1))

        with self.assertRaises(ValidationError):
            article.full_clean()

    def test_create_article_when_title_starts_with_lower_case_expect_to_raise(self):
        article = self._create_article(self.VALID_ARTICLE_DATA, title='some invalid title')

        with self.assertRaises(ValidationError):
            article.full_clean()

    def test_slug_successfully_created(self):
        article = self._create_article(self.VALID_ARTICLE_DATA)
        article.full_clean()
        article.save()

        self.assertEquals(article.slug, f'some-valid-title-{article.id}')

    def test__str__method_returns_correct_string(self):
        article = self._create_article(self.VALID_ARTICLE_DATA)
        article.full_clean()
        article.save()

        self.assertEquals(str(article), article.title)
