# Generated by Django 4.1.3 on 2022-11-26 06:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='gallery_pics', verbose_name='Фотография')),
                ('description', models.CharField(max_length=50, verbose_name='Подпись')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата загрузки')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pictures', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('favorites', models.ManyToManyField(blank=True, related_name='favorite_pics', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
