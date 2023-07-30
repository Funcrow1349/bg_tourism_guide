from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', include('bg_tourism_guide.auth_app.urls')),
    path('', include('bg_tourism_guide.common.urls')),
    path('articles/', include('bg_tourism_guide.articles.urls')),
    path('destinations/', include('bg_tourism_guide.destinations.urls')),
    path('photos/', include('bg_tourism_guide.photos.urls')),
]
