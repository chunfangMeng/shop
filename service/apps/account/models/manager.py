from django.contrib.auth.models import User
from django.db import models

from apps.account.models.member import GENDER_CLASSIFY


class ManagerUser(models.Model):
    user = models.OneToOneField(User, db_index=True, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=48, db_index=True, help_text='昵称')
    profile_photo = models.CharField(max_length=128, null=True, blank=True, help_text='头像')
    manage_number = models.CharField(max_length=24, db_index=True, help_text="编号")
    phone = models.CharField(max_length=24, null=True, blank=True, help_text="联系方式")
    gender = models.IntegerField(default=0, choices=GENDER_CLASSIFY, help_text="性别")

    class Meta:
        db_table = 'manager_user'

    def __str__(self):
        return f'{self.user.username} - {self.manage_number}'
