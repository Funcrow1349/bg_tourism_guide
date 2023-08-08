from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from bg_tourism_guide.destinations.forms import DestinationForm
from bg_tourism_guide.destinations.models import Destination
from bg_tourism_guide.photos.models import Photo


class DestinationDetailsView(DetailView):
    model = Destination
    template_name = 'destinations/destination_details.html'
    context_object_name = 'destination'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        destination = self.get_object()
        context['related_photos'] = Photo.objects.filter(tagged_destinations=destination)
        return context


class AddDestination(LoginRequiredMixin, CreateView):
    template_name = 'destinations/add_destination.html'
    form_class = DestinationForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('destination details', kwargs={'slug': self.object.slug})


class DestinationEditView(LoginRequiredMixin, UpdateView):
    model = Destination
    form_class = DestinationForm
    template_name = 'destinations/edit_destination.html'

    def get_success_url(self):
        return reverse('destination details', kwargs={'slug': self.object.slug})


class DestinationDeleteView(LoginRequiredMixin, DeleteView):
    model = Destination
    template_name = 'destinations/delete_destination.html'
    success_url = reverse_lazy('browse destinations')
