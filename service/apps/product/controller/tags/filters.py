from django.utils import timezone
from django.db.models import Q
from django_filters import rest_framework as filters

from apps.product.models.product import GoodsTag


class GoodsTagFilter(filters.FilterSet):
    """标签筛选"""
    start_date = filters.DateTimeFilter(field_name='create_at', lookup_expr='gte')
    end_date = filters.DateTimeFilter(method='end_date_filter')
    keyword = filters.CharFilter(method='keyword_filter')

    def end_date_filter(self, queryset, name, value):
        oneday = timezone.timedelta(days=1)
        end_time = value + oneday
        return queryset.filter(create_at__lte=end_time)

    def keyword_filter(self, queryset, name, value):
        return queryset.filter(Q(name__icontains=value) | Q(content__icontains=value))

    class Meta:
        model = GoodsTag
        fields = ['keyword', ]
