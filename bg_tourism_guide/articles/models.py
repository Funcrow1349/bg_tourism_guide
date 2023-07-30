from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify
from bg_tourism_guide.destinations.models import Destination

CustomUser = get_user_model()


class Article(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    body = models.TextField(null=False, blank=False)
    article_image = models.URLField(null=False, blank=False)
    tagged_destinations = models.ManyToManyField(Destination, blank=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, editable=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f'{self.title}-{self.id}')
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-updated', '-created']