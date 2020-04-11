from django.contrib import auth
from django.shortcuts import render

def index(request):
    return render(request, "index/index.html", {'username': auth.get_user(request).username})
