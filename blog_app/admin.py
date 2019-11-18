from django.contrib import admin
from .forms import BlogPostForm
# Register your models here.
from .models import Profile, BlogPost

admin.site.register(Profile)
admin.site.register(BlogPost)
