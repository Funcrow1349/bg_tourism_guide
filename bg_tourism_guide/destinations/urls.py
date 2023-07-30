from django.urls import path, include

from bg_tourism_guide.destinations.views import \
    AddDestination, DestinationEditView, DestinationDeleteView, DestinationDetailsView

urlpatterns = (
    path('add/', AddDestination.as_view(), name='add destination'),
    path('<slug:slug>/', include([
        path('', DestinationDetailsView.as_view(), name='destination details'),
        path('edit/', DestinationEditView.as_view(), name='edit destination'),
        path('delete/', DestinationDeleteView.as_view(), name='delete destination'),
    ])),
)

