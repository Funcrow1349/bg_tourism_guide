from django import forms

from bg_tourism_guide.articles.models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'body', 'article_image', 'tagged_destinations']

        labels = {
            'title': '',
            'body': '',
            'article_image': '',
            'tagged_destinations': 'Choose one or multiple destinations to tag in this article:',
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title'}),
            'body': forms.Textarea(attrs={'placeholder': 'Write your content here...'}),
            'article_image': forms.TextInput(attrs={'placeholder': 'Paste photo URL here...'})
        }