from django.urls import path
from bg_tourism_guide.common.views import index_view, gallery_view, destinations_view, articles_view

urlpatterns = (
    path('', index_view, name='index'),
    path('gallery/', gallery_view, name='browse gallery'),
    path('destinations/', destinations_view, name='browse destinations'),
    path('articles/', articles_view, name='browse articles'),
)
