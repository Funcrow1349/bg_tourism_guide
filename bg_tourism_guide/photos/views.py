from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DeleteView

from bg_tourism_guide.common.forms import CommentForm
from bg_tourism_guide.photos.forms import PhotoCreateForm
from bg_tourism_guide.photos.models import Photo


class AddPhoto(LoginRequiredMixin, CreateView):
    template_name = 'photos/create_photo.html'
    form_class = PhotoCreateForm

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

    def get_success_url(self):
        return reverse('photo page', kwargs={'pk': self.object.id})


class DeletePhoto(LoginRequiredMixin, DeleteView):
    model = Photo
    template_name = 'photos/delete_photo.html'
    success_url = reverse_lazy('browse gallery')

    # def get_queryset(self):
    #     return self.model.objects.filter(uploaded_by=self.request.user)


def photo_page(request, pk):
    photo = Photo.objects.get(pk=pk)
    form = CommentForm(request.POST or None)
    comments = photo.comment_set.all()
    tags = photo.tagged_destinations.all()

    if form.is_valid():
        comment = form.save(commit=False)
        comment.to_photo = photo

        if request.user.is_authenticated:
            comment.comment_author = request.user

        comment.save()
        return redirect('photo page', pk=pk)

    context = {
        'photo': photo,
        'form': form,
        'comments': comments,
        'tags': tags,
    }

    return render(request, 'photos/photo_page.html', context)

