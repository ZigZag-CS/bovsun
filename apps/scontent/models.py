from django.conf import settings
from django.db import models


class Content(models.Model):
    # on_delete=models.CASCADE/   https://stackoverflow.com/questions/38388423/what-does-on-delete-do-on-django-models
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='content_created', on_delete=models.CASCADE)
    title = models.CharField(max_length=180, unique=True, verbose_name='Введите загаловок')
    slug = models.SlugField(max_length=220, db_index=True, verbose_name='Slug')
    image = models.ImageField(upload_to='users/%Y/%m/%d', blank=True, null=True, default='no_image_app_content.png',
                              verbose_name='Загрузить изображение')
    entry = models.TextField(blank=True, verbose_name='Запись')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
