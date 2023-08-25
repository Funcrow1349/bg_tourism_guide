from django.contrib.auth import get_user_model
from django.db import models
from bg_tourism_guide.articles.models import Article
from bg_tourism_guide.destinations.models import Destination
from bg_tourism_guide.photos.models import Photo

CustomUser = get_user_model()


class Comment(models.Model):
    TEXT_MAX_LENGTH = 300
    text = models.TextField(max_length=TEXT_MAX_LENGTH)
    date_time_of_publication = models.DateTimeField(auto_now_add=True)
    comment_author = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    to_photo = models.ForeignKey(to=Photo, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date_time_of_publication']

