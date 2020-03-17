from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


# Create your models here.
class Post(models.Model):
    title = models.CharField(
        verbose_name="Title",
        max_length=100
    )
    text_content = models.TextField(
        verbose_name="Content"
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
    author = models.ForeignKey(
        to=User,
        related_name="posts",
        on_delete=models.CASCADE
    )
    likes = models.ManyToManyField(
        verbose_name='likes',
        to=User,
        related_name='liked_posts',
        blank=True
    )

    def __str__(self):
        return f'Post: {self.title} by {self.author}'
