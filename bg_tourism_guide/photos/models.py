from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models
from bg_tourism_guide.destinations.models import Destination

CustomUser = get_user_model()


class Photo(models.Model):
    photo = models.URLField(max_length=1000)
    description = models.TextField(
        max_length=300,
        validators=[
            MinLengthValidator(10, )
        ],
        null=True,
        blank=True,
    )
    location = models.CharField(max_length=30, blank=True, null=True)
    tagged_destinations = models.ManyToManyField(Destination, blank=True)
    date_of_publication = models.DateField(auto_now=True)
    uploaded_by = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date_of_publication']
