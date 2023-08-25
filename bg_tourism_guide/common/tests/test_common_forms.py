from django.test import TestCase

from bg_tourism_guide.common.forms import CommentForm
from bg_tourism_guide.common.models import Comment


class CommentFormTests(TestCase):

    def test_comment_form_when_data_is_valid(self):
        data = {
            'text': 'some random text'
        }

        form = CommentForm(data)
        self.assertTrue(form.is_valid())

    def test_comment_form_when_data_is_invalid_expect_to_raise(self):
        invalid_text = 't' * (Comment.TEXT_MAX_LENGTH + 1)

        data = {
            'text': invalid_text,
        }

        form = CommentForm(data)
        self.assertFalse(form.is_valid())
