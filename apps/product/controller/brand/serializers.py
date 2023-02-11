from apps.product.models.product import GoodsBrand

from rest_framework import serializers


class BranSerializer(serializers.ModelSerializer):
    create_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    last_update = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = GoodsBrand
        fields = '__all__'
