import os
from django.contrib.auth import login, views
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from bg_tourism_guide.auth_app.forms import CustomUserCreationForm, UserEditForm
from bg_tourism_guide.auth_app.models import CustomUser


class ProfileCreateView(CreateView):
    template_name = 'auth_app/create_profile_page.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save(commit=False)
        user.save()
        login(self.request, user)
        return response


class ProfileLoginView(views.LoginView):
    template_name = 'auth_app/login.html'

    def get_success_url(self):
        return reverse_lazy('index')


class ProfileLogoutView(views.LogoutView):

    def get_success_url(self):
        return reverse_lazy('index')


class ProfileEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = CustomUser
    form_class = UserEditForm
    template_name = 'auth_app/edit_profile_page.html'
    success_url = reverse_lazy('index')

    def test_func(self):
        return self.request.user == self.get_object()

    def get_object(self, queryset=None):
        queryset = queryset or self.get_queryset()
        obj = get_object_or_404(queryset, pk=self.request.user.pk)
        return obj

    def form_valid(self, form):
        profile_picture = self.request.FILES.get('profile_picture')
        if profile_picture:
            user = form.save(commit=False)
            filename = f"{user.username}_profile_picture{os.path.splitext(profile_picture.name)[1]}"
            user.profile_picture.save(filename, profile_picture)
        return super().form_valid(form)


class ProfileDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = CustomUser
    template_name = 'auth_app/delete_profile_page.html'
    success_url = reverse_lazy('index')

    def test_func(self):
        return self.request.user == self.get_object()

    def get_object(self, queryset=None):
        queryset = queryset or self.get_queryset()
        obj = get_object_or_404(queryset, pk=self.request.user.pk)
        return obj

    def delete(self, request, *args, **kwargs):
        user = self.object
        user.destination_set.all().delete()
        user.photo_set.all().delete()
        user.article_set.all().delete()
        user.comment_set.all().delete()

        return super().delete(request, *args, **kwargs)


class ProfileDetailsView(DetailView):
    model = CustomUser
    template_name = 'auth_app/profile_details.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.object
        destinations = user.destination_set.all()
        articles = user.article_set.all()
        photos = user.photo_set.all()
        context['destinations'] = destinations
        context['articles'] = articles
        context['photos'] = photos
        return context
