from apps.product.models.product import GoodsBindTag, GoodsTag

from rest_framework import serializers


class GoodsTagsSerializer(serializers.ModelSerializer):
    create_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    last_update = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    goods_bind_count = serializers.SerializerMethodField()

    def get_goods_bind_count(self, instance):
        return GoodsBindTag.objects.filter(tag=instance).count()

    class Meta:
        model = GoodsTag
        fields = ('name', 'content', 'index', 'text_color', 'back_color', 'create_at', 'last_update',
                  'goods_bind_count')
