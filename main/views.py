from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .models import Stories, Post

from .serializers import StorySerializer, PostSerializer, PostImage, PostImageSerializer

"""Function-Based-View"""
# @api_view(['GET'])
# def stories(request):
#     stories = Stories.objects.all()
#     serializer = StorySerializer(stories, many=True)
#     return Response(serializer.data)
"""Class-Based-View(APIViews)"""
# class PostListView(APIView):
#     def get(self, request):
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         post = request.data
#         serializer = PostSerializer(data=post)
#         if serializer.is_valid(raise_exception=True):
#             post_saved = serializer.save()
#         return Response(serializer.data)

"""Class-Based_View(generic views)"""


class StoriesListView(generics.ListAPIView):
    queryset = Stories.objects.all()
    serializer_class = StorySerializer


class PostView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostUpdateView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDeleteView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostImageView(generics.ListAPIView):
    queryset = PostImage.objects.all()
    serializer_class = PostImageSerializer

    def get_serializer_context(self):
        return {'request': self.request}



















