from django.contrib import admin

# Register your models here.
from app.post.models import Post, Comment, FriendRequest

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(FriendRequest)
