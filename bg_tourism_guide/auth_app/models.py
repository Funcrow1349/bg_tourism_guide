from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models
from bg_tourism_guide.auth_app.validators import is_only_letters, starts_with_uppercase


class CustomUser(AbstractUser):
    NAME_MAX_LENGTH = 30
    NAME_MIN_LENGTH = 2
    GENDERS = (
        ('Male', 'MALE'),
        ('Female', 'FEMALE'),
        ('Other', 'OTHER')
    )

    first_name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        validators=[
            MinLengthValidator(NAME_MIN_LENGTH),
            is_only_letters,
            starts_with_uppercase,
        ],
    )
    last_name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        validators=[
            MinLengthValidator(NAME_MIN_LENGTH),
            is_only_letters,
            starts_with_uppercase,
        ],
    )

    username = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=15, choices=GENDERS, null=True,)
    bio = models.TextField(null=True, blank=True,)
    profile_picture = models.ImageField(upload_to='images', null=True, default="default-profile-picture.png")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
