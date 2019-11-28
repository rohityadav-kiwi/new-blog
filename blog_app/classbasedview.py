from django.contrib.auth.models import User
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework.settings import api_settings

from .permissions import IsOwnerOrReadOnly
from .models import BlogPost
from .serializers import BlogPostSerializer, UserPostSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, permissions


class BlogList(APIView, LimitOffsetPagination):
    """
    List all snippets, or create a new snippet.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        pagination_class = api_settings.DEFAULT_PAGINATION_CLASS
        paginator = pagination_class()
        queryset = BlogPost.objects.all()
        page = paginator.paginate_queryset(queryset, request)
        # paginated_data = self.paginate_queryset(snippets, request)
        serializer = BlogPostSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = BlogPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class BlogDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    permission_classes = [permissions.IsAuthenticated, ]

    def get_object(self, pk):
        try:
            return BlogPost.objects.get(pk=pk)
        except BlogPost.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        blog = self.get_object(pk)
        serializer = BlogPostSerializer(blog)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        blog = self.get_object(pk)
        serializer = BlogPostSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        blog = self.get_object(pk)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserPostSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserPostSerializer

