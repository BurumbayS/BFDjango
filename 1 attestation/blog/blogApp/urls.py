from django.urls import path, re_path
from blogApp import views

urlpatterns = [
    path('', views.blog),
    path('addComment/', views.addComment),
    path('addPost/', views.addPost),
    path('auth/login/', views.login),
    path('auth/logout/', views.logout),
    path('auth/signup/', views.signup),
]
