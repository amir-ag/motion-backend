from rest_framework import serializers

from app.post.models import posts
from app.users.serializers import UserSerializer


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    amount_of_likes = serializers.SerializerMethodField()

    def get_amount_of_likes(self, post):
        return post.likes.all().count()

    class Meta:
        model = posts
        fields = "__all__"
