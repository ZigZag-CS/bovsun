import datetime
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


def image_profile_directory_path(instance, filename):
    time = str(datetime.date.today())
    return 'users_profiles/{0}/{1}/{2}'.format(instance.user.username, time, filename)


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    about_me = models.TextField(blank=True, max_length=160, help_text="Максимум 160 символов.")
    photo = models.ImageField(upload_to=image_profile_directory_path, blank=True, null=True,
                              default='no_image_app_content.png')

    def __str__(self):
        return "Мой профиль {}".format(self.user.username)
