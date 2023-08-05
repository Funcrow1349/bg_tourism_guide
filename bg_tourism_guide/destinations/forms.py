from django import forms

from bg_tourism_guide.destinations.models import Destination


class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = ['name', 'type', 'location', 'destination_image', 'description']

        labels = {
            'name': '',
            'type': 'Choose type of destination:',
            'location': '',
            'destination_image': '',
            'description': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Destination Name'}),
            'location': forms.TextInput(attrs={'placeholder': 'Enter Location...'}),
            'destination_image': forms.TextInput(attrs={'placeholder': 'Paste photo URL here...'}),
            'description': forms.Textarea(attrs={'placeholder': 'Write Description here...'}),
        }
