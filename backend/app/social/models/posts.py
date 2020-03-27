from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


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
    image = models.ImageField(
        verbose_name='image',
        blank=True,
        upload_to=''
    )
    likes = models.ManyToManyField(
        verbose_name='likes',
        to=User,
        related_name='liked_posts',
        blank=True
    )
    shared = models.ForeignKey(
        verbose_name='shared_post',
        to='self',
        related_name='sharing_posts',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    def __str__(self):
        return f'Post: {self.title} by {self.author}'
