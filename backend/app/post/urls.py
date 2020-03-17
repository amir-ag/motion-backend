"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path

from app.post.views import ListCreate, RetrieveUpdateDestroy, ToggleLike, UserLikedPosts, PostsByUser, \
    GetPostsofFollowing
from app.users.views import GetAllUsers, FollowToggle, ListFollowers, ListFollowees

urlpatterns = [
    path('posts/', ListCreate.as_view()),
    path('posts/<int:post_id>/', RetrieveUpdateDestroy.as_view()),
    path('posts/toggle-like/<int:post_id>/', ToggleLike.as_view()),
    path('posts/likes/', UserLikedPosts.as_view()),
    path('posts/following/', GetPostsofFollowing.as_view()),
    path('posts/user/<int:user_id>', PostsByUser.as_view()),
    path('users/', GetAllUsers.as_view()),
    path('followers/toggle-follow/<int:user_id>/', FollowToggle.as_view()),
    path('followers/followers/', ListFollowers.as_view()),
    path('followers/following/', ListFollowees.as_view())
]
