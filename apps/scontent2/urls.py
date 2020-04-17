from django.conf.urls import url
from django.urls import path
from apps.scontent2 import views

app_name = 'scontent2'

urlpatterns = [
    path('create/', views.content_create2, name='create_scontent'),

    path('detail/<int:id>/<slug:slug>/', views.content_detail2, name='detail'),
    # url(r'^detail/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.content_detail, name='detail'),
    path('detail/<int:id>/<slug:slug>/edit/', views.content_edit2, name='edit_detail'),
]