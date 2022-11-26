from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from gallery_app.models import Picture


class PictureListView(ListView):
    model = Picture
    template_name: str = 'index.html'
    context_object_name = 'pictures'
    ordering = '-created_at'


class PicrureAddView(CreateView):
    model = Picture
    template_name: str = 'picure_add.html'

