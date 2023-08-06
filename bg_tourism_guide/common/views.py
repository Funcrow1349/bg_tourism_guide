from django.shortcuts import render
from bg_tourism_guide.articles.models import Article
from bg_tourism_guide.destinations.models import Destination
from bg_tourism_guide.photos.models import Photo


def index_view(request):
    photos = Photo.objects.all()[0:3]
    destinations = Destination.objects.all()[0:3]
    articles = Article.objects.all()[0:1]

    context = {
        'photos': photos,
        'destinations': destinations,
        'articles': articles,
    }

    return render(request, 'common/index.html', context)


def gallery_view(request):
    photos = Photo.objects.all()
    return render(request, 'common/gallery.html', {'photos': photos})


def destinations_view(request):
    destinations = Destination.objects.all()
    return render(request, 'common/browse_destinations.html', {'destinations': destinations})


def articles_view(request):
    articles = Article.objects.all()
    return render(request, 'common/browse_articles.html', {'articles': articles})
