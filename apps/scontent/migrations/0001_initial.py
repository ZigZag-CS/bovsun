# Generated by Django 3.0.5 on 2020-04-17 15:00

import apps.scontent.models
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
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=180, unique=True, verbose_name='Введите загаловок')),
                ('slug', models.SlugField(max_length=220, verbose_name='Slug')),
                ('image', models.ImageField(blank=True, default='no_image_app_content.png', null=True, upload_to=apps.scontent.models.image_directory_path, verbose_name='Загрузить изображение')),
                ('entry', models.TextField(blank=True, verbose_name='Запись')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='content_created', to=settings.AUTH_USER_MODEL)),
                ('users_like', models.ManyToManyField(blank=True, related_name='contents_liked', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
