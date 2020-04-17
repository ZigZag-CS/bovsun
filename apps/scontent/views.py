# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from apps.scontent.forms import *


@login_required
def content_create(request):
    if request.method == 'POST':
        form = ContentCreateForm(request.POST, request.FILES)
        if form.is_valid():
            new_content = form.save(commit=False)
            new_content.user = request.user
            new_content.save()
            return redirect(new_content.get_absolute_url())
    else:
        form = ContentCreateForm()
    return render(request, 'scontent/create.html', {'form': form})


def content_detail(request, id, slug):
    content_detail = get_object_or_404(Content, id=id, slug=slug)
    return render(request,
                  "scontent/detail.html",
                  {'content_detail': content_detail}
                  )


@login_required
def content_edit(request, id, slug):
    new_content = get_object_or_404(Content, id=id, slug=slug)
    if new_content.user == request.user and not request.user.is_superuser:
        pass

    if request.method == 'POST':
        form = ContentCreateForm(instance=new_content, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect(new_content.get_absolute_url())
    else:
        form = ContentCreateForm(instance=new_content)
    context = {'form': form, 'create': False}
    return render(request, 'scontent/create.html', context)
