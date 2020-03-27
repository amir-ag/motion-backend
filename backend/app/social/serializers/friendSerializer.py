from rest_framework import serializers
from app.social.models import FriendRequest
from app.users.serializers import UserSerializer


class FriendSerializer(serializers.ModelSerializer):
    requester = UserSerializer(read_only=True)
    receiver = UserSerializer(read_only=True)

    class Meta:
        model = FriendRequest
        fields = '__all__'
