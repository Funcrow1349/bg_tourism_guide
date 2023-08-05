from django import forms
from bg_tourism_guide.photos.models import Photo


class PhotoCreateForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['photo', 'description', 'location', 'tagged_destinations']

        labels = {
            'photo': '',
            'description': '',
            'location': '',
            'tagged_destinations': 'Select destinations to tag in this photo:'
        }
        widgets = {
            'photo': forms.TextInput(attrs={'placeholder': 'Paste photo URL here...'}),
            'description': forms.Textarea(attrs={'placeholder': 'Write photo description...'}),
            'location': forms.TextInput(attrs={'placeholder': 'Add location...'})
        }
