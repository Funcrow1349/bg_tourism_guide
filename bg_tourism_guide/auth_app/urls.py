from django.urls import path

from bg_tourism_guide.auth_app.views import \
    ProfileCreateView, ProfileLoginView, ProfileLogoutView, ProfileEditView, ProfileDetailsView, ProfileDeleteView

urlpatterns = (
    path('create/', ProfileCreateView.as_view(), name='user create'),
    path('edit/<int:pk>/', ProfileEditView.as_view(), name='user edit'),
    path('delete/<int:pk>/', ProfileDeleteView.as_view(), name='user delete'),
    path('details/<int:pk>/', ProfileDetailsView.as_view(), name='user details'),
    path('login/', ProfileLoginView.as_view(), name='login'),
    path('logout/', ProfileLogoutView.as_view(), name='logout'),
)
