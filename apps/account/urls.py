from django.urls import path, re_path
from apps.account import views

app_name = 'account'

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    # re_path('dashboard/', views.dashboard, name='dashboard'),
    path('edit/', views.edit_profile, name="edit"),
    # users
    path('users/', views.user_list, name='user_list'),
    # user follow
    path('users/follow', views.user_follow, name='user_follow'),
    # re_path(r'^users/(?P<username>[-\w]+)/$', views.user_detail, name='user_detail'),
    path('users/<username>/', views.user_detail, name='user_detail'),
]
