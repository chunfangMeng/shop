from apps.product.models.product import GoodsAttributes, GoodsAttributesGroup
from apps.product.controller.attr.serializers import GoodsAttributesSerializer, GoodsAttrGroupSerializer
from drf.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin, RetrieveModelMixin, UpdateModelMixin

from rest_framework import status
from rest_framework.viewsets import GenericViewSet

from drf.response import JsonResponse


class GoodsAttributesView(GenericViewSet, ListModelMixin, CreateModelMixin, DestroyModelMixin, RetrieveModelMixin,
                          UpdateModelMixin):
    permission_classes = []
    serializer_class = GoodsAttributesSerializer
    queryset = GoodsAttributes.objects.order_by('-id')


class GoodsAttrGroupView(GenericViewSet, ListModelMixin, CreateModelMixin, DestroyModelMixin, RetrieveModelMixin,
                         UpdateModelMixin):
    permission_classes = ()
    serializer_class = GoodsAttrGroupSerializer
    queryset = GoodsAttributesGroup.objects.order_by('-id')

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        GoodsAttributes.objects.filter()
        self.perform_destroy(instance)
        return JsonResponse(status=status.HTTP_204_NO_CONTENT)
