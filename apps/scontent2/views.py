# -*- coding: utf-8 -*-
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from apps.scontent2.forms import *
from my_decorators.decorator_ajax import *


@login_required
def content_create2(request):
    if request.method == 'POST':
        form = ContentCreateForm2(request.POST, request.FILES)
        if form.is_valid():
            new_content = form.save(commit=False)
            new_content.user = request.user
            new_content.save()
            return redirect(new_content.get_absolute_url())
    else:
        form = ContentCreateForm2()
    return render(request, 'scontent2/create.html', {'form': form})


def content_detail2(request, id, slug):
    content_detail = get_object_or_404(Content2, id=id, slug=slug)
    return render(request,
                  "scontent2/detail.html",
                  {'content_detail2': content_detail}
                  )


@login_required
def content_edit2(request, id, slug):
    new_content = get_object_or_404(Content2, id=id, slug=slug)
    if new_content.user == request.user and not request.user.is_superuser:
        pass

    if request.method == 'POST':
        form = ContentCreateForm2(instance=new_content, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect(new_content.get_absolute_url())
    else:
        form = ContentCreateForm2(instance=new_content)
    context = {'form': form, 'create_scontent2': False}
    return render(request, 'scontent2/create.html', context)


@login_required
def delete_content2(request, id, slug):
    new_to_delete = get_object_or_404(Content2, id=id, slug=slug)

    if new_to_delete.user != request.user and not request.user.is_superuser:
        messages.error(request, "Эту запись вы не создавали, не можете удалить.")
        return redirect(new_to_delete.get_absolute_url())

    if request.method == 'POST':
        form = DeleteContentForms2(request.POST, instance=new_to_delete)

        if form.is_valid():
            new_to_delete.delete()
            messages.success(request, 'Запись успешно удалена')
            return HttpResponseRedirect('/')

    else:
        form = DeleteContentForms2(instance=new_to_delete)

    tempate_vars = {'form': form}
    return render(request, 'scontent2/delete.html', tempate_vars)


@login_required
@require_POST
@ajax_required
def content_like(request):
    content_id = request.POST.get('id')
    action = request.POST.get('action')

    if content_id and action:
        try:
            content = Content2.objects.get(id=content_id)
            if action == 'like':
                content.users_like.add(request.user)
                # adaugam in lenta
            else:
                content.users_like.remove(request.user)

            # JSON
            return JsonResponse({'status': 'ok'})
        except:
            pass

    return JsonResponse({'status': 'ko'})
