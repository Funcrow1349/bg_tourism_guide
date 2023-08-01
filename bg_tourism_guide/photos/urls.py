from django.urls import path

from bg_tourism_guide.photos.views import DeletePhoto, AddPhoto, photo_page

urlpatterns = (
    path('add/', AddPhoto.as_view(), name='add photo'),
    path('delete/<int:pk>', DeletePhoto.as_view(), name='delete photo'),
    path('photo/<int:pk>', photo_page, name='photo page')
)
