from django.urls import path

from apps.index import views

app_name = 'index'

urlpatterns = [
    path('', views.index, name='home_page'),
]
