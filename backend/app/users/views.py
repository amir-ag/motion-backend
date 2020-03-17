from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.response import Response

from app.users.models import User
from app.users.serializers import UserSerializer


class GetAllUsers(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class FollowToggle(GenericAPIView):
    serializer_class = UserSerializer
    lookup_url_kwarg = 'user_id'
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        user_to_follow = self.get_object()
        user = request.user

        if user in user_to_follow.followees.all():
            user_to_follow.followees.remove(user)
            return Response(self.get_serializer(instance=user_to_follow).data)
        user_to_follow.followees.add(user)
        return Response(self.get_serializer(instance=user_to_follow).data)

class ListFollowers(ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(followees=self.request.user)

class ListFollowees(ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(followers=self.request.user)