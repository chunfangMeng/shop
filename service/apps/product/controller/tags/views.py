from django_filters import rest_framework as filters

from apps.product.controller.tags.filters import GoodsTagFilter
from apps.product.controller.tags.serializers import GoodsTagsSerializer
from apps.product.models.product import GoodsTag
from drf.mixins import CreateModelMixin, DestroyModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin

from rest_framework.viewsets import GenericViewSet


class GoodsTagsView(GenericViewSet, CreateModelMixin, DestroyModelMixin, ListModelMixin, RetrieveModelMixin,
                    UpdateModelMixin):
    permission_classes = ()
    serializer_class = GoodsTagsSerializer
    queryset = GoodsTag.objects.order_by('-id')
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = GoodsTagFilter

