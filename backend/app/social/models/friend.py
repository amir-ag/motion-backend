from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class FriendRequest(models.Model):
    requester = models.ForeignKey(
        verbose_name='requester',
        to=User,
        related_name='requests_sent',
        on_delete=models.CASCADE
    )
    receiver = models.ForeignKey(
        verbose_name='receiver',
        to=User,
        related_name='requests_received',
        on_delete=models.CASCADE
    )
    status = models.CharField(
        verbose_name='status',
        max_length=1,
        choices=(
            ('P', 'pending'),
            ('A', 'accepted'),
            ('D', 'declined'),
        ),
        default='P'
    )

    class Meta:
        unique_together = ['requester', 'receiver']

    def __str__(self):
        return f'{self.requester}, {self.receiver}, {self.status}'
