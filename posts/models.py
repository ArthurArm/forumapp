from django.contrib.auth import get_user_model
from django.db import models

from posts.choices import LanguageChoices
from posts.validators import BadWordValidator


# Create your models here.
UserModel = get_user_model()


class Post(models.Model):
    TITLE_MAX_LENGTH = 100
    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
    )

    content = models.TextField(
        validators=[
            BadWordValidator(
                bad_words=[
                    "bad_word1",
                    "bad_word2",
                ]
            )
        ]
    )

    author = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
    )

    created_at = models.DateField(
        auto_now_add=True,
    )

    language = models.CharField(
        max_length=20,
        choices=LanguageChoices.choices,
        default=LanguageChoices.OTHER,
    )

    image = models.ImageField(
        upload_to='media_files/',
        blank=True,
        null=True,
    )

    approved = models.BooleanField(
        default=False,
    )

    class Meta:
        permissions = [
            ('approve_post', 'Can approve post'),
        ]


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
    )

    author = models.CharField(
        max_length=100,
    )

    content = models.TextField()

    created_at = models.DateField(
        auto_now_add=True,
    )
