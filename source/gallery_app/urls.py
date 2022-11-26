from django.urls import path
from gallery_app.views import PictureListView


urlpatterns = [
    path('', PictureListView.as_view(), name='index_view'),
]