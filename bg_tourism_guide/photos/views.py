from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView

from bg_tourism_guide.photos.forms import PhotoCreateForm
from bg_tourism_guide.photos.models import Photo


class AddPhoto(LoginRequiredMixin, CreateView):
    template_name = 'photos/create_photo.html'
    form_class = PhotoCreateForm
    success_url = reverse_lazy('browse gallery')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.method in ('POST', 'PUT'):
            kwargs.update({
                'data': self.request.POST,
                'files': self.request.FILES,
            })
        return kwargs

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)


class DeletePhoto(LoginRequiredMixin, DeleteView):
    model = Photo
    template_name = 'photos/delete_photo.html'
    success_url = reverse_lazy('browse_gallery')

    def get_queryset(self):
        return self.model.objects.filter(uploaded_by=self.request.user)

