from django.db import models
from django.contrib.auth.models import User


class GoodsBrand(models.Model):
    """商品品牌"""
    en_name = models.CharField(max_length=64, db_index=True, help_text='英文品牌名')
    zh_name = models.CharField(max_length=64, db_index=True, help_text='中文品牌名')
    url_path = models.CharField(max_length=36, help_text='URL名称')
    create_at = models.DateTimeField(auto_now_add=True, help_text='创建日期')
    last_update = models.DateTimeField(auto_now=True, help_text='最新一次更新')

    class Meta:
        db_table = 'goods_brand'


class GoodsBrandContext(models.Model):
    """商品品牌内容"""
    goods_brand = models.ForeignKey(GoodsBrand, on_delete=models.CASCADE, help_text='品牌')
    content = models.TextField(null=True, blank=True, help_text="内容描述")

    class Meta:
        db_table = 'goods_brand_context'


class GoodsBrandImage(models.Model):
    """商品品牌图片"""
    IMAGE_CLASSIFY = (
        (0, '缩略图'),
        (1, '品牌横幅')
    )
    goods_brand = models.ForeignKey(GoodsBrand, on_delete=models.CASCADE, help_text='品牌')
    classify = models.IntegerField(default=0, choices=IMAGE_CLASSIFY)
    image = models.TextField(help_text="图片")

    class Meta:
        db_table = 'goods_brand_image'


class GoodsAttributesGroup(models.Model):
    """商品属性组"""
    name = models.CharField(max_length=36, help_text="属性组名称")
    alias = models.CharField(max_length=36, help_text="别名")
    attr_index = models.IntegerField(default=0, help_text="排序")
    create_at = models.DateTimeField(auto_now_add=True, help_text='创建日期')
    last_update = models.DateTimeField(auto_now=True, help_text='最新一次更新')

    class Meta:
        db_table = 'goods_attributes_group'


class GoodsAttributes(models.Model):
    """商品属性"""
    name = models.CharField(max_length=36, help_text="属性名称")
    alias = models.CharField(max_length=36, help_text="别名")
    attr_index = models.IntegerField(default=0, help_text="排序")
    attr_group = models.ForeignKey(GoodsAttributesGroup, on_delete=models.CASCADE, help_text="属性组")
    create_at = models.DateTimeField(auto_now_add=True, help_text='创建日期')
    last_update = models.DateTimeField(auto_now=True, help_text='最新一次更新')

    class Meta:
        db_table = 'goods_attributes'


class GoodsClassify(models.Model):
    """商品分类"""
    name = models.CharField(max_length=48, unique=True, db_index=True, help_text="商品分类名称")
    url_path = models.CharField(max_length=36, db_index=True, help_text="URl名称")
    parent_classify = models.CharField(max_length=48, null=True, blank=True, help_text="上级分类")
    create_at = models.DateTimeField(auto_now_add=True, help_text='创建日期')
    last_update = models.DateTimeField(auto_now=True, help_text='最新一次更新')

    class Meta:
        db_table = 'goods_classify'


class GoodsTag(models.Model):
    """商品标签"""
    name = models.CharField(max_length=32, unique=True, help_text="标签名称")
    content = models.CharField(max_length=64, null=True, blank=True, help_text="标签描述")
    index = models.IntegerField(default=0, help_text="标签排序")
    create_at = models.DateTimeField(auto_now_add=True, help_text='创建日期')
    last_update = models.DateTimeField(auto_now=True, help_text='最新一次更新')

    class Meta:
        db_table = 'goods_tag'


class PriceLevelGroup(models.Model):
    """商品价格分组"""
    code = models.CharField(max_length=36, unique=True, db_index=True, help_text="价格组代码")
    name = models.CharField(max_length=36, unique=True, db_index=True, help_text='价格组名称')
    note = models.CharField(max_length=128, null=True, blank=True, help_text='价格组备注')
    create_at = models.DateTimeField(auto_now_add=True, help_text='创建日期')
    last_update = models.DateTimeField(auto_now=True, help_text='最新一次更新')

    class Meta:
        db_table = 'price_level_group'


class DiscountAmount(models.Model):
    """价格组 - 折扣"""
    PERMISSION_TYPE = (
        (0, '公开'),
        (1, '私有')
    )
    discount_code = models.CharField(max_length=36, unique=True, db_index=True, help_text="折扣代码")
    quota = models.FloatField(default=0, help_text="折扣额度")
    note = models.CharField(max_length=128, null=True, blank=True, help_text="折扣备注")
    permissions = models.IntegerField(default=0, choices=PERMISSION_TYPE, help_text="权限")
    level_group = models.ForeignKey(PriceLevelGroup, on_delete=models.CASCADE, help_text='')
    update_date = models.DateTimeField(auto_now=True, help_text="更新时间")
    updater = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, help_text="更新人")

    class Meta:
        db_table = 'discount_amount'


class DiscountAmountUser(models.Model):
    """价格组 - 折扣绑定用户"""
    discount = models.ForeignKey(DiscountAmount, on_delete=models.SET_NULL, null=True, blank=True, help_text="折扣")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, help_text="用户")
    bind_date = models.DateTimeField(auto_now_add=True, help_text="绑定日期")
    binding_person = models.ForeignKey(User, related_name="binding_person", on_delete=models.SET_NULL, null=True,
                                       blank=True, help_text="绑定人")
    update_date = models.DateTimeField(auto_now=True, help_text="最后更新日期")

    class Meta:
        db_table = 'discount_amount_user'


class Goods(models.Model):
    """商品表"""
    GOODS_CLASSIFY = (
        (0, '整箱待发'),
        (1, '单品选购')
    )
    sku = models.CharField(max_length=36, db_index=True, help_text="SKU")
    zh_name = models.CharField(max_length=128, db_index=True, unique=True, help_text="中文名称")
    en_name = models.CharField(max_length=256, null=True, blank=True, help_text="英文名称")
    sub_name = models.CharField(max_length=128, null=True, blank=True, help_text="副标题")
    classify = models.IntegerField(default=0, choices=GOODS_CLASSIFY, help_text="下单模式")
    url_path = models.CharField(max_length=48, unique=True, help_text="URL链接")
    goods_index = models.IntegerField(default=0, help_text="排序")
    is_sell_well = models.BooleanField(default=False, help_text="是否是热销")
    goods_classify = models.ForeignKey(GoodsClassify, on_delete=models.SET_NULL, null=True, blank=True, help_text="分类")
    goods_brand = models.ForeignKey(GoodsBrand, on_delete=models.SET_NULL, null=True, blank=True, help_text="品牌")
    gbp_amount = models.DecimalField(decimal_places=0, max_digits=10, help_text="英镑零售价")
    discount_gbp_amount = models.DecimalField(decimal_places=0, max_digits=10, help_text="英镑活动价")
    tax_gbp_amount = models.DecimalField(decimal_places=0, max_digits=10, help_text="英镑商品税费")
    freight_gbp_amount = models.DecimalField(decimal_places=0, max_digits=10, help_text="英镑商品运费")
    last_update = models.DateTimeField(auto_now=True, help_text="最新更新日期")
    create_at = models.DateTimeField(auto_now_add=True, help_text="创建日期")

    class Meta:
        db_table = 'goods'


class GoodsBindTag(models.Model):
    """商品关联标签"""
    goods = models.ForeignKey(Goods, on_delete=models.SET_NULL, null=True, blank=True, help_text="商品")
    tag = models.ForeignKey(GoodsTag, on_delete=models.SET_NULL, null=True, blank=True, help_text="商品标签")
    create_at = models.DateTimeField(auto_now_add=True, help_text='创建日期')
    last_update = models.DateTimeField(auto_now=True, help_text='最新一次更新')

    class Meta:
        db_table = 'goods_bind_tag'


class GoodsBindAttr(models.Model):
    """商品关联属性"""
    goods = models.ForeignKey(Goods, on_delete=models.SET_NULL, null=True, blank=True, help_text="商品")
    goods_attr = models.ManyToManyField(GoodsAttributes, blank=True, help_text="商品属性")
    create_at = models.DateTimeField(auto_now_add=True, help_text='创建日期')
    last_update = models.DateTimeField(auto_now=True, help_text='最新一次更新')

    class Meta:
        db_table = 'goods_bind_attr'


class DiscountLevelGoods(models.Model):
    """商品关联商品价格分组"""
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, help_text='商品')
    price_level_group = models.ForeignKey(PriceLevelGroup, on_delete=models.CASCADE, help_text='商品价格分组')
    create_at = models.DateTimeField(auto_now_add=True, help_text='创建日期')
    last_update = models.DateTimeField(auto_now=True, help_text='最新一次更新')

    class Meta:
        db_table = 'discount_level_goods'


