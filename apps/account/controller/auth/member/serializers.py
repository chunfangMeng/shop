from rest_framework.validators import UniqueValidator

from django.contrib.auth.models import User
from rest_framework import serializers

from apps.account.models.member import UserMember


class UserSerializers(serializers.ModelSerializer):
    def validate(self, data):
        if not data.get('email'):
            raise serializers.ValidationError("邮箱不能为空")
        return data

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email', 'is_staff', 'is_active']
        extra_kwargs = {
            'username': {
                'error_messages': {
                    'blank': '请输入用户名'
                }
            },
            'password': {
                'write_only': True,
                'min_length': 8,
                'error_messages': {
                    'blank': '请输入密码'
                }
            },
            'email': {
                'validators': [
                    UniqueValidator(
                        queryset=User.objects.all().order_by('id'),
                        message='该邮箱已被注册'
                    ),
                ],
            },
            'is_staff': {
                'write_only': True,
            },
            'is_active': {
                'write_only': True,
            }
        }


class UserMemberSerializers(serializers.ModelSerializer):
    user = UserSerializers()

    class Meta:
        model = UserMember
        fields = '__all__'

