from django.shortcuts import render
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *
from .permission import isAuthor
from .models import Author
from rest_framework import permissions


class PostsListAPIView(generics.ListCreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return (isAuthor(),)
        return super().get_permissions()

    def perform_create(self, serializer):
        """ Метод створює новий пост. При цьому, здійснюється перевірка чи існує автор, який відповідає зареєстрованому
        автору. Якщо відповідний автор існує, то створюється пост. У протелижному випадку повертається помилка 404.
        """
        author_ints = get_object_or_404(Author, name = self.request.user)
        serializer.save(author = author_ints)


class AuthorListAPIView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAdminUser]


class AuthorDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class PostsAPIUpdate(generics.UpdateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    permission_classes = [isAuthor]

class PostsAPIDestroy(generics.DestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    permission_classes = [isAuthor]


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
