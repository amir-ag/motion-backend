from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from app.social.models import FriendRequest
from app.social.serializers.friendSerializer import FriendSerializer

User = get_user_model()

# Create a new friend request

class CreateFriendRequest(CreateAPIView):
    """
    post:
    Create a new pending friend request.
    """
    queryset = User.objects.all()
    serializer_class = FriendSerializer
    lookup_url_kwarg = 'user_id'

    def create(self, request, *args, **kwargs):
        receiver = self.get_object()
        requester = request.user
        friendship = FriendRequest(requester=requester, receiver=receiver)
        friendship.save()
        return Response(self.get_serializer(instance=friendship).data)

# get/update/delete a specific friend request


class GetFriendRequest(RetrieveUpdateDestroyAPIView):
    lookup_url_kwarg = 'friend_request_id'
    queryset = FriendRequest.objects.all()
    serializer_class = FriendSerializer

