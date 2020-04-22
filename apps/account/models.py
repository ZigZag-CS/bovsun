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


class Contact(models.Model):
    # ForeignKey для пользователя, который создает отношения
    user_from = models.ForeignKey(User, related_name='rel_from_set', on_delete=models.CASCADE)
    # пользователь к которому создают отношение
    user_to = models.ForeignKey(User, related_name='rel_to_set', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return '{} follows {}'.format(self.user_from, self.user_to)


# Adaugam camp dinamic in User
"""
prin intermediul la Contact, cand symmetrical=False, cand o parte devine falower la alta parte, 
din cealalta parte se face automat asta
"""
User.add_to_class('following',
                  models.ManyToManyField('self', through=Contact, related_name='followers', symmetrical=False))
