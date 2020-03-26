from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView, ListAPIView
from rest_framework.response import Response

from app.post.models import Post
from app.post.serializers import PostSerializer


class ListCreate(ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class RetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    lookup_url_kwarg = 'post_id'
    queryset = Post.objects.filter()


class ToggleLike(GenericAPIView):
    serializer_class = PostSerializer
    lookup_url_kwarg = 'post_id'
    queryset = Post.objects.all()

    def post(self, request, *args, **kwargs):
        relevant_post = self.get_object()
        user = request.user
        if user in relevant_post.likes.all():
            relevant_post.likes.remove(user.id)
            return Response(self.get_serializer(instance=relevant_post).data)
        relevant_post.likes.add(user.id)
        return Response(self.get_serializer(instance=relevant_post).data)


class UserLikedPosts(ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        return self.request.user.liked_posts


class PostsByUser(ListAPIView):
    serializer_class = PostSerializer
    lookup_url_kwarg = 'user_id'

    def get_queryset(self):
        user = self.kwargs['user_id']
        return Post.objects.filter(author=user)

class GetPostsofFollowing(ListCreate):
    serializer_class = PostSerializer

    def get_queryset(self):
        followed_user_ids = self.request.user.followees.all().values_list("id", flat=True)
        return Post.objects.filter(author__in=followed_user_ids)


class ListCreateComments(ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_url_kwarg = 'post_id'
