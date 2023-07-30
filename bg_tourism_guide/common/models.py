from django.contrib.auth import get_user_model
from django.db import models
from bg_tourism_guide.articles.models import Article
from bg_tourism_guide.destinations.models import Destination

CustomUser = get_user_model()


# class BaseComment(models.Model):
#     text = models.TextField(max_length=300)
#     date_time_of_publication = models.DateField(auto_now_add=True)
#     # user = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
#
#     class Meta:
#         ordering = ['-date_time_of_publication']
#
#
# class DestinationComment(BaseComment):
#     # to_destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
#     pass
#
#
# class ArticleComment(BaseComment):
#     # to_destination = models.ForeignKey(Article, on_delete=models.CASCADE)
#     pass
#
#
# class PhotoComment(BaseComment):
#     pass
