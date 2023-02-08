import base64

from drf.response import JsonResponse
from rest_framework.viewsets import GenericViewSet
from captcha.views import CaptchaStore, captcha_image


class CaptchaView(GenericViewSet):
    authentication_classes = []
    permission_classes = []

    def list(self, request):
        hash_key = CaptchaStore.generate_key()
        captcha_obj = CaptchaStore.objects.filter(hashkey=hash_key).first()
        if not captcha_obj:
            return JsonResponse(code=4021, message="请稍后再试")
        captcha_img = captcha_image(request, hash_key)
        base64_obj = base64.b64encode(captcha_img.content)
        return JsonResponse(data={
            'hash_key': hash_key,
            'base64_image': base64_obj.decode('utf-8')
        })