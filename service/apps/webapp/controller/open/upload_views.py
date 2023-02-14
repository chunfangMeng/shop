from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet

from drf.response import JsonResponse


class UpLoadView(GenericViewSet):
    authentication_classes = []
    permission_classes = []

    @action(methods=['get'], detail=False, url_path='section/ready')
    def section_ready(self, request):
        md5_key = request.GET.get('md5_key')
        return JsonResponse()

    @action(methods=['post'], detail=False, url_path='section/fragment')
    def section_fragment(self, request):
        return JsonResponse()

    @action(methods=['get'], detail=False, url_path='section/finish')
    def section_finish(self, request):
        return JsonResponse()

    @action(methods=['post'], detail=False)
    def upload(self, request):
        return JsonResponse()
