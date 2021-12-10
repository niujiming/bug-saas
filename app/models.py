from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserInfo(AbstractUser):
    phone = models.CharField(verbose_name='手机号', max_length=11)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        # 在admin后台中显示的名称
        verbose_name_plural = '用户表'

    def __str__(self):
        return self.username
