from apps.product.models.product import PriceLevelGroup
from apps.product.controller.price.serializers import PriceGroupSerializer
from drf.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin

from rest_framework.viewsets import GenericViewSet


class GoodsPriceGroupView(GenericViewSet, CreateModelMixin, ListModelMixin, RetrieveModelMixin):
    permission_classes = []
    serializer_class = PriceGroupSerializer
    queryset = PriceLevelGroup.objects.order_by('-id')
