from django.urls import path, include

from bg_tourism_guide.articles.views import AddArticle, ArticleDetailsView, ArticleEditView, ArticleDeleteView

urlpatterns = (
    path('add/', AddArticle.as_view(), name='add article'),
    path('<slug:slug>/', include([
        path('', ArticleDetailsView.as_view(), name='article details'),
        path('edit/', ArticleEditView.as_view(), name='edit article'),
        path('delete/', ArticleDeleteView.as_view(), name='delete article'),
    ])),
)
