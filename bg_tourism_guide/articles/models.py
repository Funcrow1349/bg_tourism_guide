from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models
from django.template.defaultfilters import slugify
from bg_tourism_guide.auth_app.validators import starts_with_uppercase
from bg_tourism_guide.destinations.models import Destination

CustomUser = get_user_model()


class Article(models.Model):
    TITLE_MAX_LENGTH = 120
    TITLE_MIN_LENGTH = 12
    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
        validators=[MinLengthValidator(TITLE_MIN_LENGTH), starts_with_uppercase],
        null=False,
        blank=False
    )
    body = models.TextField(null=False, blank=False)
    article_image = models.URLField(max_length=1000, null=False, blank=False)
    tagged_destinations = models.ManyToManyField(Destination, blank=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, editable=False)

    # create slug automatically
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f'{self.title}-{self.id}')
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-updated', '-created']