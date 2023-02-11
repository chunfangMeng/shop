from apps.product.controller.brand import views as brand_views
from apps.product.controller.attr import views as goods_attr_views
from apps.product.controller.tags import views as goods_tag_view

from rest_framework.routers import SimpleRouter

urlpatterns = [

]

router = SimpleRouter()

router.register('brand', brand_views.GoodsBrandView, basename='product_brand')
router.register('attributes', goods_attr_views.GoodsAttributesView, basename='goods_attributes')
router.register('attr/group', goods_attr_views.GoodsAttrGroupView, basename='goods_attr_group')
router.register('goods/tags', goods_tag_view.GoodsTagsView, basename='goods_tag')

urlpatterns += router.urls
