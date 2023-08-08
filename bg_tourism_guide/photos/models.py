from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

from bg_tourism_guide.auth_app.validators import starts_with_uppercase
from bg_tourism_guide.destinations.models import Destination

CustomUser = get_user_model()


class Photo(models.Model):
    DESCRIPTION_MAX_LENGTH = 300
    DESCRIPTION_MIN_LENGTH = 10
    LOCATION_MAX_LENGTH = 50
    photo = models.URLField(max_length=1000, null=False, blank=False)
    description = models.TextField(
        max_length=DESCRIPTION_MAX_LENGTH,
        validators=[
            MinLengthValidator(DESCRIPTION_MIN_LENGTH),
            starts_with_uppercase,
        ],
        null=True,
        blank=True,
    )
    location = models.CharField(
        max_length=LOCATION_MAX_LENGTH,
        validators=[
            starts_with_uppercase,
        ],
        null=True,
        blank=True,
    )
    tagged_destinations = models.ManyToManyField(Destination, blank=True)
    date_of_publication = models.DateField(auto_now=True)
    uploaded_by = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date_of_publication']
