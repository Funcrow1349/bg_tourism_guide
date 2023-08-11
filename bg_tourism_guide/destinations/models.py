from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models
from django.template.defaultfilters import slugify

from bg_tourism_guide.auth_app.validators import starts_with_uppercase

CustomUser = get_user_model()


class Destination(models.Model):
    DESTINATION_NAME_MAX_LENGTH = 120
    DESTINATION_NAME_MIN_LENGTH = 2
    LOCATION_MAX_LENGTH = 50
    TYPES = (
        ('Natural Site', 'NATURAL SITE'),
        ('History and Heritage', 'HISTORY AND HERITAGE'),
        ('Beach area', 'BEACH AREA'),
        ('Winter Sports', 'WINTER SPORTS'),
        ('Art and Culture', 'ART AND CULTURE'),
        ('Event', 'EVENT'),
        ('Architecture', 'ARCHITECTURE'),
    )

    name = models.CharField(
        max_length=DESTINATION_NAME_MAX_LENGTH,
        validators=[
            MinLengthValidator(DESTINATION_NAME_MIN_LENGTH),
            starts_with_uppercase,
        ],
        null=False,
        blank=False)
    type = models.CharField(max_length=30, choices=TYPES, null=False, blank=False)
    location = models.CharField(
        max_length=LOCATION_MAX_LENGTH,
        validators=[
            starts_with_uppercase,
        ],
        null=False,
        blank=False
    )
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    destination_image = models.URLField(max_length=1000, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, editable=False)

    # automatically create slug
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f'{self.name}-{self.id}')
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-updated', '-created']


