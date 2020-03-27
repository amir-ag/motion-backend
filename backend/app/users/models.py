from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from app import settings


class User(AbstractUser):
    USERNAME_FIELD = 'email'

    # Additional fields required when using createsuperuser (USERNAME_FIELD and passwords are always required)
    REQUIRED_FIELDS = ['username']

    email = models.EmailField(
        unique=True
    )
    username = models.CharField(
        verbose_name='username',
        max_length=200,
        unique=True
    )
    first_name = models.CharField(
        verbose_name='first name',
        max_length=200,
        blank=True,
    )
    last_name = models.CharField(
        verbose_name='last name',
        max_length=200,
        blank=True,
    )
    is_staff = models.BooleanField(
        verbose_name='staff status',
        default=False,
        help_text='Designates whether the user can log into this site.',
    )
    is_active = models.BooleanField(
        verbose_name='active',
        default=True,
        help_text='Designates whether this user should be treated as active. '
                  'Unselect this instead of deleting accounts.'
    )
    date_joined = models.DateTimeField(
        verbose_name='date joined',
        auto_now_add=True
    )

    location = models.CharField(
        verbose_name='user location',
        max_length=200,
        blank=True
    )

    about_me = models.CharField(
        verbose_name='user description',
        max_length=1000,
        blank=True
    )

    job = models.CharField(
        verbose_name='job title',
        max_length=200,
        blank=True
    )

    followees = models.ManyToManyField(
        verbose_name='followees',
        to=settings.AUTH_USER_MODEL,
        related_name='followers',
        blank=True
    )

    def __str__(self):
        return self.username