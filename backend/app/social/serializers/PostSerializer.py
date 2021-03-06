from rest_framework import serializers

from app.social.models import Post
from app.users.serializers import UserSerializer


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    amount_of_likes = serializers.SerializerMethodField()

    @staticmethod
    def get_amount_of_likes(self, post):
        return post.likes.all().count()

    class Meta:
        model = Post
        fields = "__all__"
