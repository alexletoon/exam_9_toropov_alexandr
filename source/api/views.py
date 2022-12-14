from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from gallery_app.models import Picture
from api.serializers import PictureSerializer
from django.contrib.auth.models import User
from django.http import JsonResponse



class PicturesAPI(ModelViewSet):
    model = Picture
    serializer_class = PictureSerializer


    def add_favorites(self, request, *args, **kwargs):
        picture = get_object_or_404(Picture, pk=kwargs.get('pk'))
        user = self.request.user
        # serializer = PictureSerializer
        user.favorite_pics.add(picture)
        return JsonResponse({'Message': 'Add to favorite'})


    def remove_favorites(self, request, *args, **kwargs):
        picture = get_object_or_404(Picture, pk=kwargs.get('pk'))
        user = self.request.user
        user.favorite_pics.remove(picture)
        return JsonResponse({'Message': 'Remove from favorites'})

