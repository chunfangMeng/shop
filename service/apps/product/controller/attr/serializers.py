from apps.product.models.product import GoodsAttributes, GoodsAttributesGroup

from rest_framework import serializers


class GoodsAttributesSerializer(serializers.ModelSerializer):
    create_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    last_update = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = GoodsAttributes
        fields = '__all__'


class GoodsAttrGroupSerializer(serializers.ModelSerializer):
    create_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    last_update = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    attr_count = serializers.SerializerMethodField()

    def get_attr_count(self, instance):
        return GoodsAttributes.objects.filter(attr_group=instance).count()

    class Meta:
        model = GoodsAttributesGroup
        fields = ('name', 'alias', 'attr_index', 'create_at', 'last_update', 'attr_count')
