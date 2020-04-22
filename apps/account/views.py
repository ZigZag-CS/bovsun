from django.contrib import auth, messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
# from django.contrib.auth.models import User
# from django.template import RequestContext
from django.views.decorators.http import require_POST

from apps.account.forms import *
from apps.account.models import *
from my_decorators.decorator_ajax import ajax_required


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('account:dashboard')
                    # return redirect('/')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login and password')
    else:
        form = LoginForm()
    return render(request, "account/login.html", {'form': form, 'username': auth.get_user(request).username})


def user_logout(request):
    auth.logout(request)
    return redirect('/')


@login_required
def dashboard(request):
    # context = RequestContext(request)
    to = User.objects.get(username=request.user)
    try:
        profile = Profile.objects.get(user=to)
    except ObjectDoesNotExist:
        profile = None
    return render(request, "account/dashboard.html",
                  {
                      'username': auth.get_user(request).username,
                      'to': to,
                      'profile': profile,
                      'user': request.user,
                      'fullname': request.user.get_full_name,
                      'email': request.user.email,
                      'last_name': request.user.last_name,
                      'first_name': request.user.first_name,
                      'ip_address': request.META['REMOTE_ADDR'],
                  }
                  )


@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)

        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Профиль успешно обновлён.')
            return redirect('account:dashboard')
        else:
            messages.error(request, 'Ой! Ошибка при обновлении профиля. Попробуйте снова.')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, "account/edit.html",
                  {
                      'user_form': user_form,
                      'profile_form': profile_form
                  }
                  )


@login_required
def user_list(request):
    users = User.objects.filter(is_active=True)

    return render(request,
                  'account/user/users_list.html',
                  {'users': users})


@login_required
def user_detail(request, username):
    user = get_object_or_404(User,
                             username=username,
                             is_active=True)

    return render(request,
                  'account/user/detail_user.html',
                  {'user': user})

@ajax_required
@require_POST
@login_required
def user_follow(request):
    user_id = request.POST.get('id')
    action = request.POST.get('action')
    if user_id and action:
        try:
            user = User.objects.get(id=user_id)
            if action == 'follow':
                Contact.objects.get_or_create(user_from=request.user, user_to=user)
                #create_action(request.user, 'is following', user)# добавит в ленту за кем пользователь слудует


            else:
                Contact.objects.filter(user_from=request.user, user_to=user).delete()



            return JsonResponse({'status':'ok'})
        except User.DoesNotExist:
            return JsonResponse({'status':'ko'})
    return JsonResponse({'status':'ko'})