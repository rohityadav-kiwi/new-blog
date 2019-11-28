""" django urls are checked here"""
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .classbasedview import BlogList, BlogDetail, UserDetail, UserList

urlpatterns = [
    path("blog/", BlogList.as_view(), name='blog_list'),
    path('blog/<int:pk>/', BlogDetail.as_view(), name='blog_detail'),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
