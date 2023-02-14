from django.contrib.auth.models import User
from django.db import models


GENDER_CLASSIFY = (
    (0, '未知'),
    (1, '男'),
    (2, '女'),
    (3, '保密')
)


class UserMember(models.Model):
    user = models.OneToOneField(User, db_index=True, on_delete=models.CASCADE)
    member_no = models.CharField(max_length=24, db_index=True, help_text="会员号")
    phone = models.CharField(max_length=24, null=True, blank=True, help_text="联系方式")
    gender = models.IntegerField(default=0, choices=GENDER_CLASSIFY, help_text="性别")

    class Meta:
        db_table = 'user_member'

    def __str__(self):
        return f'{self.user} - {self.member_no}'