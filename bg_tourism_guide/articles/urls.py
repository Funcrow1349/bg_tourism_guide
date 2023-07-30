from django.urls import path, include

from bg_tourism_guide.articles.views import AddArticle, article_details, edit_article, delete_article

urlpatterns = (
    path('add/', AddArticle.as_view(), name='add article'),
    path('<slug:article_slug>/', include([
        path('', article_details, name='article details'),
        path('edit/', edit_article, name='edit article'),
        path('delete/', delete_article, name='delete article'),
    ])),
)
