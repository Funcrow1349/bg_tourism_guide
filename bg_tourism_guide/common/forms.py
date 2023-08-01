from django import forms

from bg_tourism_guide.common.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {
            'text': 'Comment:'
        }
        widgets = {
            'text': forms.TextInput(attrs={'placeholder': 'Write your comment here...'})
        }
