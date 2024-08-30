from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser


class User(AbstractBaseUser):
    username = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    score = models.IntegerField(default=0)

    USERNAME_FIELD = 'nickname'

    class Meta:
        db_table = "User"


class Player(models.Model):
    nickname = models.CharField(max_length=50, unique=True, verbose_name='Nickname')
    password = models.CharField(max_length=128, verbose_name='Password')
    score = models.IntegerField(default=0, verbose_name='Score')

    def __str__(self):
        return self.nickname