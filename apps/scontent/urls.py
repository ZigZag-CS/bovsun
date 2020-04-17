from django.conf.urls import url
from django.urls import path
from apps.scontent import views

app_name = 'scontent'

urlpatterns = [
    path('create/', views.content_create, name='create_scontent'),

    path('detail/<int:id>/<slug:slug>/', views.content_detail, name='detail'),
    # url(r'^detail/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.content_detail, name='detail'),
    # path('detail/<int:id>/<slug:slug>/edit/', views.content_edit, name='edit_detail'),
]