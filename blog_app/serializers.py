from django.contrib.auth import authenticate
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator
#
# from .models import BlogPost, Profile
#
#
# class UserSerializer(serializers.ModelSerializer):
#     email = serializers.EmailField(required=True,
#                                    validators=[UniqueValidator(queryset=User.objects.all())]
#                                    )
#     username = serializers.CharField(max_length=32, validators=[UniqueValidator(queryset=User.objects.all())]
#                                      )
#     password = serializers.CharField(required=True, min_length=8, write_only=True)
#
#     def create(self, validated_data):
#         user = User.objects.create_user(validated_data['username'],
#                                         validated_data['email'],
#                                         validated_data['password'])
#         Token.objects.create(user=user)
#         return user
#
#     class Meta:
#         model = Profile
#         fields = ('id', 'username', 'email', 'password')
#
#
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
#
#
# class LoginSerializer(serializers.ModelSerializer):
#     username = serializers.CharField(required=True)
#     password = serializers.CharField(required=True)
#
#     class Meta:
#         model = User
#         fields = ['username', 'password']
#
#     def validate(self, attrs):
#         user = authenticate(username=attrs['username'], password=attrs['password'])
#         if not user:
#             raise serializers.ValidationError("User doesn't exist or invalid password ")
#         return attrs
#
# #
# # class AuthorPostSerializer(serializers.ModelSerializer):
# #     posts = serializers.SerializerMethodField()
# #
# #     class Meta:
# #         model = User
# #         fields = ['id', "username", 'posts']
#
#
# class UserPostSerializer(serializers.ModelSerializer):
#     posts = serializers.PrimaryKeyRelatedField(many=True, queryset=BlogPost.objects.all())
#
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'snippets']
