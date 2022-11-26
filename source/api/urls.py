from django.urls import path
from rest_framework import routers
# from api.views import AddToFavoritesView
from api.views import PicturesAPI

urlpatterns = [
    path('picture_favorites/add/<int:pk>/', PicturesAPI.as_view({'get': 'add_favorites'}), name='favorites_add'),
    path('picture_favorites/remove/<int:pk>/', PicturesAPI.as_view({'get': 'remove_favorites'}), name='favorites_remove'),

]
