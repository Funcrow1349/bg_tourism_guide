from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from bg_tourism_guide.articles.forms import ArticleForm
from bg_tourism_guide.articles.models import Article


class ArticleDetailsView(DetailView):
    model = Article
    template_name = 'articles/article_details.html'
    context_object_name = 'article'


class AddArticle(LoginRequiredMixin, CreateView):
    template_name = 'articles/add_article.html'
    form_class = ArticleForm

    # set author automatically upon creation
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('article details', kwargs={'slug': self.object.slug})


class ArticleEditView(LoginRequiredMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'articles/edit_article.html'

    def get_success_url(self):
        return reverse('article details', kwargs={'slug': self.object.slug})


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'articles/delete_article.html'
    success_url = reverse_lazy('browse articles')
