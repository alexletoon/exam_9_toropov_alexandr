from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from gallery_app.models import Picture
from gallery_app.forms import PictureCreationForm
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.models import User

class PictureListView(ListView):
    model = Picture
    template_name: str = 'index.html'
    context_object_name = 'pictures'
    ordering = '-created_at'


class PictureAddView(LoginRequiredMixin, CreateView):
    model = Picture
    template_name: str = 'picture_add.html'
    form_class = PictureCreationForm
    success_url = '/'


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PictureDetailView(DetailView):
    model = Picture
    template_name: str = 'picture_detail.html'


class PictureUpdateView(UserPassesTestMixin, UpdateView):
    model = Picture
    template_name: str = 'picture_update.html'
    form_class = PictureCreationForm
    success_url = '/'

    def test_func(self):
        return self.request.user == self.get_object().author or self.request.user.is_superuser or self.request.user.has_perm('gallery_app.change_picture')


class PictureDeleteView(UserPassesTestMixin, DeleteView):
    model = Picture
    template_name: str = 'picture_confirm_delete.html'
    success_url = '/'

    def test_func(self):
        return self.request.user == self.get_object().author or self.request.user.is_superuser or self.request.user.has_perm('gallery_app.delete_picture')


class AddFavoritesView(View):
    def post(self, request, *args, **kwargs):
        picture = get_object_or_404(Picture, pk=kwargs.get('pk'))
        user = self.request.user
        if not User.objects.filter(favorite_pics=picture).exists():
            user.favorite_pics.add(picture)
        else: 
            user.favorite_pics.remove(picture)
        return redirect('index_view')

