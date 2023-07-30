from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify

CustomUser = get_user_model()


class Destination(models.Model):
    TYPES = (
        ('Natural Site', 'NATURAL SITE'),
        ('History and Heritage', 'HISTORY AND HERITAGE'),
        ('Beach area', 'BEACH AREA'),
        ('Winter Sports', 'WINTER SPORTS'),
        ('Art and Culture', 'ART AND CULTURE'),
        ('Event', 'EVENT'),
        ('Architecture', 'ARCHITECTURE'),
    )

    name = models.CharField(max_length=200, null=False, blank=False)
    type = models.CharField(max_length=30, choices=TYPES, null=False, blank=False)
    location = models.CharField(max_length=200, null=False, blank=False)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    destination_image = models.URLField()
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, editable=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f'{self.name}-{self.id}')
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-updated', '-created']


