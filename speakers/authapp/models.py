from datetime import timedelta

from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.contrib.auth.models import PermissionsMixin
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now

from rest_framework.authtoken.models import Token as BaseToken

from workroomsapp.models import Person
from .managers import UserManager


class User(AbstractUser, PermissionsMixin):
    username = None
    first_name = None
    last_name = None
    email = models.EmailField(max_length=254, unique=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    activation_key = models.CharField(max_length=128, null=True, blank=True)
    activation_key_expires = models.DateTimeField(auto_now_add=True, blank=True, null=True) # Жень, уточни параметр auto_now_add=True. Кажется это поле не должно быть по умолчанию "просроченым"
    is_authenticated = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.email

    def login(self):
        self.is_authenticated = True
        self.save()
        return self

    def logout(self):
        self.is_authenticated = False
        self.save()
        return self

    def is_activation_key_expired(self):
        now_date = now() - timedelta(hours=24)
        if now_date <= self.activation_key_expires:
            return False
        return True

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            User.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.user.save()

class Token(BaseToken):
    user = models.OneToOneField(
        User,
        related_name='auth_token',
        on_delete=models.CASCADE
    )


