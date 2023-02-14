import pytz

from apps.product.models.product import GoodsBindTag, GoodsTag
from datetime import datetime

from rest_framework import serializers


class GoodsTagsSerializer(serializers.ModelSerializer):
    create_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    last_update = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    goods_bind_count = serializers.SerializerMethodField()

    def get_goods_bind_count(self, instance):
        return GoodsBindTag.objects.filter(tag=instance).count()

    def to_internal_value(self, data):
        data['last_update'] = datetime.now().astimezone(pytz.timezone('Europe/London'))
        return data

    class Meta:
        model = GoodsTag
        fields = ('id', 'name', 'content', 'index', 'text_color', 'back_color', 'create_at', 'last_update',
                  'goods_bind_count')
