from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from app.post.models import FriendRequest
from app.post.serializers.friendSerializer import FriendSerializer

User = get_user_model()


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

