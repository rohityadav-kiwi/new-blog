
from rest_framework import serializers
from django.contrib.auth.models import User

from .models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = BlogPost
        fields = ['id', 'author', 'title', 'post_content', 'is_published']


class UserPostSerializer(serializers.ModelSerializer):
    # blog = serializers.PrimaryKeyRelatedField(many=True, queryset=BlogPost.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username']
