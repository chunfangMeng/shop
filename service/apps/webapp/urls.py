from apps.webapp.controller.open import upload_views
from apps.webapp.controller.open.captcha_views import CaptchaView

from rest_framework.routers import SimpleRouter

urlpatterns = []

router = SimpleRouter()

router.register('captcha', CaptchaView, basename='captcha_view')
router.register('upload', upload_views.UpLoadView, basename='upload_view')

urlpatterns += router.urls
