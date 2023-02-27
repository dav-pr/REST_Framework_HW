from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *


# Create your views here.

# Для розуміння, як це працює під капотом
# class PostsAPIview(generics.ListAPIView)
#     queryset = Posts.objects.all()
#     serializer_class = PostsSerializer


# class PostsAPIView(APIView):
#     def get(self, request):
#         w = Posts.objects.all()
#         return Response({'posts': PostsSerializer(w, many=True).data})
#
#     def post(self, request):
#         serializer = PostsSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'post': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#
#         try:
#             instance = Posts.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exists"})
#
#         serializer = PostsSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method DELETE not allowed"})
#
#         # здесь код для удаления записи с переданным pk
#
#         return Response({"post": "delete post " + str(pk)})

class PostsListAPIView(generics.ListCreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer


class AuthorListAPIView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class PostsAPIUpdate(generics.UpdateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer


class PostsAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer


class CommentsAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommetnsSerializer


class LikePostAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LikePost.objects.all()
    serializer_class = LikePostSerializer


class LikeCommentsAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LikeComments.objects.all()
    serializer_class = LikeCommentsSerializer
