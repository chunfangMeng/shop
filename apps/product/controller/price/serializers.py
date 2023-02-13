from apps.product.models import PriceLevelGroup, DiscountAmount, DiscountLevelGoods

from rest_framework import serializers


class PriceGroupSerializer(serializers.ModelSerializer):
    create_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    last_update = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    discount_amount = serializers.SerializerMethodField(read_only=True)
    bind_goods_count = serializers.SerializerMethodField(read_only=True)

    def get_discount_amount(self, instance):
        return DiscountAmount.objects.filter(level_group=instance).count()

    def get_bind_goods_count(self, instance):
        return DiscountLevelGoods.objects.filter(price_level_group=instance).count()

    class Meta:
        model = PriceLevelGroup
        fields = ('code', 'name', 'note', 'create_at', 'last_update', 'discount_amount', 'bind_goods_count')
