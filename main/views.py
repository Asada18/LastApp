from django.db.models import Q
from django.shortcuts import render
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, viewsets, status
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
# class PostView(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#
# class PostDetailView(generics.RetrieveAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#
# class PostUpdateView(generics.UpdateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#
# class PostDeleteView(generics.DestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#
# class StoriesListView(generics.ListAPIView):
#     queryset = Stories.objects.all()
#     serializer_class = StorySerializer


class StoriesViewSet(viewsets.ModelViewSet):
    queryset = Stories.objects.all()
    serializer_class = StorySerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=False, methods=['get'])       # router builds path posts/search/?q=word
    def search(self, request, pk=None):
        q = request.query_params.get('q')
        queryset = self.get_queryset()
        queryset = queryset.filter(Q(title__icontains=q) |
                                   Q(text__icontains=q))
        serializer = PostSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class PostImageView(generics.ListCreateAPIView):
    queryset = PostImage.objects.all()
    serializer_class = PostImageSerializer

    def get_serializer_context(self):
        return {'request': self.request}



















