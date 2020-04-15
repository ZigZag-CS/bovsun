import datetime
from django.conf import settings
from django.db import models
from django.utils.text import slugify


# from pytils.translit import slugify

def image_directory_path(instance, filename):
    time = str(datetime.date.today())
    return 'users/{0}/{1}/{2}'.format(instance.user.username, time, filename)


class Content(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='content_created', on_delete=models.CASCADE)
    title = models.CharField(max_length=180, unique=True, verbose_name='Введите загаловок')
    slug = models.SlugField(max_length=220, db_index=True, verbose_name='Slug')
    # image = models.ImageField(upload_to='users/%Y/%m/%d', blank=True, null=True,
    # default='no_image_app_content.png', verbose_name='Загрузить изображение')
    image = models.ImageField(upload_to=image_directory_path, blank=True, null=True, default='no_image_app_content.png',
                              verbose_name='Загрузить изображение')
    entry = models.TextField(blank=True, verbose_name='Запись')
    created = models.DateTimeField(auto_now_add=True)
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='contents_liked', blank=True)

    # переопределили метод save для автослуг
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
            # super(Content, self).save(*args, **kwargs)
        super(Content, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
