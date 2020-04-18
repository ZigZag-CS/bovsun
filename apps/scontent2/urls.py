from django.conf.urls import url
from django.urls import path
from apps.scontent2 import views

app_name = 'scontent2'

urlpatterns = [
    path('create/', views.content_create2, name='create_scontent2'),
    path('detail/<int:id>/<slug:slug>/', views.content_detail2, name='detail2'),
    # url(r'^detail/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.content_detail2, name='detail2'),
    path('detail/<int:id>/<slug:slug>/edit/', views.content_edit2, name='edit_detail2'),
    path('detail/<int:id>/<slug:slug>/delete/', views.delete_content2, name='delete_content2'),
]
