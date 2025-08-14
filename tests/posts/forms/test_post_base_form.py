from django.test import TestCase

from posts.choices import LanguageChoices
from posts.forms import PostBaseForm
from posts.models import Post


class TestPostBaseForm(TestCase):
    def setUp(self):
        self.data = {
            'title': 'test title',
            'content': "test content that's long enough",
            'language': LanguageChoices.OTHER,
            'image': None,
        }

    def test__form_is_valid__expect_success(self):
        form = PostBaseForm(data=self.data)
        self.assertTrue(form.is_valid())

    def test__title_is_missing__expect_custom_error_message(self):
        self.data['title'] = None
        form = PostBaseForm(data=self.data)
        self.assertFalse(form.is_valid())
        self.assertEquals(
            PostBaseForm._meta.error_messages['title']['required'],
            form.errors['title'][0]
        )

    def test__title_is_too_long__expect_custom_error_message(self):
        self.data['title'] = 'a' * (Post.TITLE_MAX_LENGTH + 1)
        form = PostBaseForm(data=self.data)
        self.assertFalse(form.is_valid())
        self.assertEquals(
            PostBaseForm._meta.error_messages['title']['max_length'],
            form.errors['title'][0]
        )

    def test__title_in_content__raises_value_error(self):
        self.data['title'] = 'title'
        self.data['content'] = 'title and something'
        form = PostBaseForm(data=self.data)

        form.is_valid()

        self.assertTrue(form.errors['__all__'])

    def test__save_form_saves_the_title_with_capital_letter(self):
        self.data['title'] = 'title'
        form = PostBaseForm(data=self.data)

        form.is_valid()
        post = form.save(commit=False)

        self.assertEquals(post.title, self.data['title'].capitalize())
