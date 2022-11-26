from rest_framework import serializers
from gallery_app.models import Picture
from django.contrib.auth.models import User


class PictureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Picture
        fields = ('id', 'image', 'description', 'created_at', 'updated_at', 'author', 'favorites')
        # read_only_fields = ('favorites',)