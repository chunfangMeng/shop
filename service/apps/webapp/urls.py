from apps.webapp.controller.open import upload_views

from rest_framework.routers import SimpleRouter

from apps.webapp.controller.open.captcha.captcha_views import CaptchaView

urlpatterns = []

router = SimpleRouter()

router.register('captcha', CaptchaView, basename='captcha_view')
# router.register('upload', upload_views.UpLoadView, basename='upload_view')

urlpatterns += router.urls
