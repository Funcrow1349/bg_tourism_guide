from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from bg_tourism_guide.articles.forms import ArticleForm


def article_details(request, article_slug):
    pass


class AddArticle(CreateView):
    template_name = 'articles/add_article.html'
    form_class = ArticleForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def edit_article(request, article_slug):
    pass


def delete_article(request, article_slug):
    pass
