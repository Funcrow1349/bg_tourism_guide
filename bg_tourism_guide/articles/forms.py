from django import forms

from bg_tourism_guide.articles.models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'body', 'article_image', 'tagged_destinations']
