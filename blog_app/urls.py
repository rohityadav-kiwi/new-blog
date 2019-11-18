from . import views
from django.urls import path
from .views import update_post, post_list, create_post, delete_post, PostDetailView, myblogs

urlpatterns = [

    path("", post_list, name='post_list'),
    path("new",create_post, name = 'create_post'),
    path('post/<int:id>/update', update_post, name='update_post'),
    path("post/<int:id>/delete", delete_post, name='delete_post'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path("myblogs", myblogs, name='my_blog'),
    path("signup/", views.signup, name='signup'),
    path("profile/" ,views.UserProfiledetails, name = 'my_profile')
]
