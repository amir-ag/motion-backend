# Create your views here.
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView, ListAPIView
from rest_framework.response import Response

from app.social.models import Post, Comment
from app.social.serializers.CommentSerializer import CommentSerializer
from app.social.serializers.PostSerializer import PostSerializer

# Get all posts or create a new one


class ListCreate(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# Get, update or delete a specific post


class RetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    lookup_url_kwarg = 'post_id'
    queryset = Post.objects.filter()

# Like or unlike a specific post

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

# Get liked posts of logged-in user


class UserLikedPosts(ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        return self.request.user.liked_posts


# Get posts of a specific user


class PostsByUser(ListAPIView):
    serializer_class = PostSerializer
    lookup_url_kwarg = 'user_id'

    def get_queryset(self):
        user = self.kwargs['user_id']
        return Post.objects.filter(author=user)

# Get posts of people the logged-in user is following


class GetPostsOfFollowing(ListCreate):
    serializer_class = PostSerializer

    def get_queryset(self):
        followed_user_ids = self.request.user.followees.all().values_list("id", flat=True)
        return Post.objects.filter(author__in=followed_user_ids)

# Get all or create a comment on a specific post


class ListCreateComments(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = CommentSerializer
    lookup_url_kwarg = 'post_id'

    def list(self, request, *args, **kwargs):
        post = self.get_object()
        comments = post.comments
        return Response(self.get_serializer(instance=comments, many=True).data)

    def create(self, request, *args, **kwargs):
        post = self.get_object()
        comment = Comment(author=request.user, post=post, comment=request.data['comment'])
        comment.save()
        return Response(self.get_serializer(instance=comment).data)
