from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """
    カスタムユーザーモデル
    """
    email = models.EmailField('メールアドレス', unique=True)
    phone_number = models.CharField('電話番号', max_length=20, blank=True)
    department = models.CharField('部署', max_length=100, blank=True)
    created_at = models.DateTimeField('作成日時', auto_now_add=True)
    updated_at = models.DateTimeField('更新日時', auto_now=True)

    class Meta:
        verbose_name = 'ユーザー'
        verbose_name_plural = 'ユーザー'

    def __str__(self):
        return self.username

