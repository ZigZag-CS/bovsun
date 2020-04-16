from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.template import RequestContext

from .forms import LoginForm
from apps.account.models import *


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
    context = RequestContext(request)
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
