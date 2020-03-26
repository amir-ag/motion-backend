from django.contrib.auth import get_user_model
from django.db import models

from app.post.models.posts import Post

User = get_user_model()


class Comment(models.Model):
    author = models.ForeignKey(
        verbose_name='author',
        to=User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    post = models.ForeignKey(
        verbose_name='post',
        to=Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    comment = models.CharField(
        verbose_name='content',
        max_length=1000
    )
    created = models.DateTimeField(
        verbose_name='created on',
        auto_now_add=True
    )

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"{self.author} post a comment: {self.comment[:20]}..."
