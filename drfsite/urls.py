"""drfsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, include, re_path
from blog.views import PostsListAPIView, AuthorListAPIView, AuthorDetailAPIView, CommentsAPIDetailView,\
    LikePostAPIDetailView, LikeCommentsAPIDetailView, PostsAPIDestroy

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/v1/postslist', PostsListAPIView.as_view(),  name ='posts_list' ),
    path('api/v1/postslist/<int:pk>/', PostsListAPIView.as_view()),
    path('api/v1/postslist/update/<int:pk>/', PostsListAPIView.as_view(),  name ='posts_update'),
    path('api/v1/postslist/detail/<int:pk>/', PostsListAPIView.as_view(),  name ='posts_detail'),
    path('api/v1/postslist/delete/<int:pk>/', PostsAPIDestroy.as_view(),  name ='posts_delete'),
    path('api/v1/author/detail/<int:pk>/', AuthorDetailAPIView.as_view(),  name ='author_detail'),
    path('api/v1/author', AuthorListAPIView.as_view(),  name ='author_list'),
    path('api/v1/comments/detail/<int:pk>/', CommentsAPIDetailView.as_view(),  name ='comments_detail'),
    path('api/v1/likepost/detail/<int:pk>/', LikePostAPIDetailView.as_view(),  name ='likepost_detail'),
    path('api/v1/likecomments/detail/<int:pk>/',LikeCommentsAPIDetailView.as_view(),  name ='likecomments_detail'),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),  # new
]
