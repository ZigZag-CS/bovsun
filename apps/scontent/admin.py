# -*- coding: utf-8 -*-
from django.contrib import admin
from apps.scontent.models import Content


class ContentAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'image', 'created']
    list_filter = ['created']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Content, ContentAdmin)
