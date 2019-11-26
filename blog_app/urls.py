""" django urls are checked here"""
from django.urls import path

from .accounts import signup, login
from .views import post_list, post_details

urlpatterns = [
    path("post", post_list, name='post_list'),
    path('post/<int:pk>/', post_details, name='post-detail'),
    path('signup/', signup, name='SignupView'),
    path('login/', login, name='loginView'),
]
