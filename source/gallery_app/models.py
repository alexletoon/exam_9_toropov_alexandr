from django.db import models
from django.contrib.auth.models import User

class Picture(models.Model):
    image = models.ImageField(verbose_name='Фотография', blank=False, null=False, upload_to='gallery_pics')
    description = models.CharField(verbose_name='Подпись', blank=False, null=False, max_length=50)
    created_at = models.DateTimeField(verbose_name='Дата загрузки', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)
    author = models.ForeignKey(verbose_name='Автор', to=User, related_name='pictures', on_delete=models.CASCADE)
    favorites = models.ManyToManyField(to=User, related_name='favorite_pics', blank=True)


    def __str__(self) -> str:
        return f'author - {self.author}, description - {self.description}'