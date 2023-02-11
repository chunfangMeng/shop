from apps.product.controller.brand.serializers import BranSerializer
from apps.product.models.product import GoodsBrand
from drf.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

from rest_framework.viewsets import GenericViewSet


class GoodsBrandView(GenericViewSet, ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin,
                     DestroyModelMixin):
    permission_classes = ()
    serializer_class = BranSerializer
    queryset = GoodsBrand.objects.order_by('-id')
