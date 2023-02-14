from django.contrib.auth.models import User
from rest_framework import serializers

from apps.account.controller.auth.member.serializers import UserSerializers
from apps.account.models.manager import ManagerUser


class ManagerUserSerializers(serializers.ModelSerializer):
    user = UserSerializers()

    def to_internal_value(self, data):
        all_user = ManagerUser.objects.all().order_by('id')
        data['manage_number'] = f'MU{str(all_user.count() + 1).zfill(5)}'
        return super().to_internal_value(data)

    def create(self, validated_data):
        user_obj = User.objects.create_user(**validated_data.get('user'))
        validated_data['user'] = user_obj
        instance = ManagerUser.objects.create(**validated_data)
        return instance

    class Meta:
        model = ManagerUser
        fields = '__all__'