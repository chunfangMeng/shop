from captcha.views import CaptchaStore
from rest_framework import serializers


class CaptchaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaptchaStore
        fields = '__all__'
