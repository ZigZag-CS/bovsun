# -*- coding: utf-8 -*-
from django import forms
from apps.scontent2.models import *


class ContentCreateForm2(forms.ModelForm):
    class Meta:
        model = Content2
        fields = ('title', 'image', 'entry',)


class DeleteContentForms2(forms.ModelForm):
    class Meta:
        model = Content2
        fields = []
