from django.urls import path
from apps.scontent import views

app_name = 'scontent'

urlpatterns = [
    path('create/', views.content_create, name='create_scontent'),

    #url(r'^detail/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.content_detail, name='detail'),
]