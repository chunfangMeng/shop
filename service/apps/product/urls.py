from apps.product.controller.brand import views as brand_views
from apps.product.controller.attr import views as goods_attr_views
from apps.product.controller.tags import views as goods_tag_view
from apps.product.controller.price import views as product_price_view

from rest_framework.routers import SimpleRouter

urlpatterns = [

]

router = SimpleRouter()

router.register('brand', brand_views.GoodsBrandView, basename='product_brand')
router.register('attributes', goods_attr_views.GoodsAttributesView, basename='goods_attributes')
router.register('attr/group', goods_attr_views.GoodsAttrGroupView, basename='goods_attr_group')
router.register('goods/tags', goods_tag_view.GoodsTagsView, basename='goods_tag')
router.register('goods/price/group', product_price_view.GoodsPriceGroupView, basename='goods_price_group')

urlpatterns += router.urls
