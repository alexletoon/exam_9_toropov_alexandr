from django.contrib import admin
from gallery_app.models import Picture

class PictureAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'description', 'created_at')
    list_filter = ('id', 'author', 'description', 'created_at')
    search_fields = ('author', 'created_at')
    fields = ('author', 'description', 'image', 'favorites')


admin.site.register(Picture, PictureAdmin)