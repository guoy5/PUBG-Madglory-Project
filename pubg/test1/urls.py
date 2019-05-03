from django.contrib import admin
from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('search_player/', views.search),
]
