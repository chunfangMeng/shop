from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet

from apps.account.controller.auth.auth_user import AuthContext, AuthClientEnum
from apps.account.controller.auth.backend.serializers import ManagerUserSerializers
from apps.account.models.manager import ManagerUser
from apps.account.models.member import GENDER_CLASSIFY
from drf.auth import ManageAuthenticate
from drf.mixins import ListModelMixin, RetrieveModelMixin
from drf.response import JsonResponse


class ManagerUserView(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    """
    后台用户视图
    """
    queryset = ManagerUser.objects.order_by('id')
    serializer_class = ManagerUserSerializers
    authentication_classes = (ManageAuthenticate,)
    auth_context = AuthContext(AuthClientEnum(0))

    @action(methods=['get'], detail=False, authentication_classes=[], permission_classes=[])
    def options(self, request):
        """
        后台用户列表筛选下拉框数据
        """
        return_data = [{
            'options': GENDER_CLASSIFY,
            'name': 'gender',
            'classify': 'select',
            'placeholder': '性别'
        }]
        return JsonResponse(data=return_data)

    @action(methods=['post'], detail=False, authentication_classes=[], permission_classes=[])
    def login(self, request):
        """
        登陆
        """
        token_key, user, message = self.auth_context.auth(request)
        response = JsonResponse(data={'token': token_key}, message=message)
        return response

    @action(methods=['get'], detail=False)
    def info(self, request):
        """
        已登陆后台账户信息
        """
        query_obj = self.get_queryset().filter(user=request.user).first()
        if not query_obj:
            return JsonResponse(message="该管理员账号不存在")
        serializers_data = self.get_serializer(query_obj)
        return JsonResponse(data=serializers_data.data)

    @action(methods=['post'], detail=False)
    def logout(self, request):
        """
        退出登陆
        """
        self.auth_context.logout(request)
        return JsonResponse(message='退出登陆成功')

    @action(methods=['post'], detail=False, authentication_classes=[], permission_classes=[])
    def register(self, request):
        """创建后台账户"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(message='创建成功', data=serializer.data)

    def update(self, request, pk):
        """更新指定后台账户信息"""
        instance = self.get_object()
        request.data['password'] = instance.user.password
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return JsonResponse(message="修改成功")

