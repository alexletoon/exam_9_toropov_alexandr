from django.urls import path
from gallery_app.views import PictureListView, PictureAddView, PictureDetailView, PictureUpdateView, PictureDeleteView, AddFavoritesView


urlpatterns = [
    path('', PictureListView.as_view(), name='index_view'),
    path('picture_add/', PictureAddView.as_view(), name='picture_add'),
    path('picture_detail/<int:pk>', PictureDetailView.as_view(), name='picture_detail'),
    path('picture_update/<int:pk>', PictureUpdateView.as_view(), name='picture_update'),
    path('picture_delete/<int:pk>', PictureDeleteView.as_view(), name='picture_delete'),
    path('picture_favorites/<int:pk>', AddFavoritesView.as_view(), name='picture_favorites'),
]