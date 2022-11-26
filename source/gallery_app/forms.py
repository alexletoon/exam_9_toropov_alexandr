from django import forms
from gallery_app.models import Picture


class PictureCreationForm(forms.ModelForm):

    class Meta:
        model = Picture
        fields = ['image', 'description']

