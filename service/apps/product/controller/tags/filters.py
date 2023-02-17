from django.utils import timezone
from django_filters import rest_framework as filters

from apps.product.models.product import GoodsTag


class GoodsTagFilter(filters.FilterSet):
    """价格模板"""
    start_date = filters.DateTimeFilter(field_name='create_time', lookup_expr='gte')
    end_date = filters.DateTimeFilter(method='end_date_filter')

    def end_date_filter(self, queryset, name, value):
        oneday = timezone.timedelta(days=1)
        end_time = value + oneday
        return queryset.filter(create_at__lte=end_time)

    class Meta:
        model = GoodsTag
        fields = {}
