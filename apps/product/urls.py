from apps.product.controller.brand import views as brand_views

from rest_framework.routers import SimpleRouter

urlpatterns = [

]

router = SimpleRouter()

router.register('brand', brand_views.GoodsBrandView, basename='product_brand')

urlpatterns += router.urls
