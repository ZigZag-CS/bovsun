from django.contrib import admin
from apps.account.models import *

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'photo']

admin.site.register(Profile, ProfileAdmin)
