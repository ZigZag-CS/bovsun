# -*- coding: utf-8 -*-
from django import forms
from apps.scontent.models import *


class ContentCreateForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ('title', 'image', 'entry',)


class DeleteContentForms(forms.ModelForm):
    class Meta:
        model = Content
        fields = []
