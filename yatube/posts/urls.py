# posts/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('group/list', views.group_list),
    path('group/<slug:slug>/', views.group_posts)
]
