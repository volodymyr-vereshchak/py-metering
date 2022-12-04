from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Position(models.IntegerChoices):
        ADMIN = 1
        ENGINEER = 2
        MASTER = 3
        LOCKSMITH = 4
        SUBSCRIBER = 5

    position = models.IntegerField(choices=Position.choices)
