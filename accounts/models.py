

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models

from accounts.managers import AppUserManager


#   option 1: Inherit the Abstract User, gives us the ability to add fields on top of existing once from Django
# class CustomUser(AbstractUser):
#     points = models.IntegerField(
#         null=True,
#         blank=True,
#     )


#   option 2: This won't create a table in database, but we can't add fields in table. We can modify the existing fields with additional validations
# class CustomCustomUser(CustomUser):
#     class Meta:
#         proxy = True
#
#         def get_points(self):
#             return self.points


#   option 3: Inherit AbstractBaseUser, which gives us full control of the fields
class AppUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
    )

    username = models.CharField(
        max_length=150,
        unique=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    objects = AppUserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(
        AppUser,
        on_delete=models.CASCADE,
    )

    age = models.IntegerField(
        null=True,
        blank=True,
    )

    points = models.IntegerField(
        null=True,
        blank=True,
    )

    phone_number = models.CharField(
        max_length=10,
        null=True,
        blank=True,
    )
