from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet

from apps.account.controller.auth.auth_user import AuthContext
from apps.account.controller.auth.member.serializers import UserMemberSerializers
from apps.account.models.member import UserMember
from drf.mixins import ListModelMixin, RetrieveModelMixin
from drf.response import JsonResponse


class UserMemberView(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = UserMember.objects.all().order_by('id')
    serializer_class = UserMemberSerializers
    auth_context = AuthContext()

    @action(detail=False, methods=['post'], authentication_classes=[], permission_classes=[])
    def login(self, request):
        token_key, user, message = self.auth_context.auth(request)
        response = JsonResponse(data={'token': token_key}, message=message)
        return response

    @action(detail=False, methods=['get'])
    def info(self, request):
        query_obj = self.get_queryset().filter(user=request.user).first()
        if not query_obj:
            return JsonResponse(message="会员不存在")
        serializers_data = self.get_serializer(query_obj)
        return JsonResponse(data=serializers_data.data)