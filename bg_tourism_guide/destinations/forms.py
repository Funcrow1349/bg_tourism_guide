from django import forms

from bg_tourism_guide.destinations.models import Destination


class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = ['name', 'type', 'location', 'destination_image', 'description']
