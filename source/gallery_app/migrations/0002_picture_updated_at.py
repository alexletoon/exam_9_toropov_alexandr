# Generated by Django 4.1.3 on 2022-11-26 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата изменения'),
        ),
    ]
