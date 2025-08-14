from django.core.exceptions import ValidationError
from django.test import TestCase

from posts.validators import BadWordValidator


class TestBadLanguageValidator(TestCase):
    def setUp(self):
        self.bad_words = [
            "bad_word1",
            "bad_word2",
        ]

        self.validator = BadWordValidator(self.bad_words)

    def test__validate_clean_message_expect_success(self):
        self.validator("clean message")

    def test__validate_explicit_content_message__expect_validation_error(self):
        with self.assertRaises(ValidationError) as ve:
            self.validator(self.bad_words[0] + ' some text')

        self.assertTrue(str(ve))
        
