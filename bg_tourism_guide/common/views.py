from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from bg_tourism_guide.articles.models import Article
from bg_tourism_guide.destinations.models import Destination
from bg_tourism_guide.photos.models import Photo


def index_view(request):
    photos = Photo.objects.all()[0:3]
    destinations = Destination.objects.all()[0:3]
    articles = Article.objects.all()[0:3]

    context = {
        'photos': photos,
        'destinations': destinations,
        'articles': articles,
    }

    return render(request, 'common/index.html', context)


def gallery_view(request):
    photos = Photo.objects.all()

    page_number = request.GET.get('page', 1)
    items_per_page = 9

    paginator = Paginator(photos, items_per_page)

    try:
        page_photos = paginator.page(page_number)
    except PageNotAnInteger:
        page_photos = paginator.page(1)
    except EmptyPage:
        page_photos = paginator.page(paginator.num_pages)

    return render(request, 'common/gallery.html', {'photos': page_photos})


def destinations_view(request):
    destination_type = request.GET.get('type', None)

    if destination_type:
        destinations = Destination.objects.filter(type=destination_type)
    else:
        destinations = Destination.objects.all()

    page_number = request.GET.get('page', 1)
    items_per_page = 6

    paginator = Paginator(destinations, items_per_page)

    try:
        page_destinations = paginator.page(page_number)
    except PageNotAnInteger:
        page_destinations = paginator.page(1)
    except EmptyPage:
        page_destinations = paginator.page(paginator.num_pages)

    return render(request, 'common/browse_destinations.html', {'destinations': page_destinations})


def articles_view(request):
    articles = Article.objects.all()

    page_number = request.GET.get('page', 1)
    items_per_page = 6

    paginator = Paginator(articles, items_per_page)

    try:
        page_articles = paginator.page(page_number)
    except PageNotAnInteger:
        page_articles = paginator.page(1)
    except EmptyPage:
        page_articles = paginator.page(paginator.num_pages)

    return render(request, 'common/browse_articles.html', {'articles': page_articles})


def custom_404(request, exception):
    return render(request, '404.html', status=404)
