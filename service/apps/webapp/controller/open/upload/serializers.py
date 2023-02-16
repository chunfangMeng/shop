from rest_framework import serializers

from apps.webapp.models import UploadImage


class UploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadImage
        fields = '__all__'
