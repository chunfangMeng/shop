from apps.product.models.product import GoodsTag

from rest_framework import serializers


class GoodsTagsSerializer(serializers.ModelSerializer):
    create_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    last_update = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = GoodsTag
        fields = ('name', 'content', 'index', 'create_at', 'last_update')
