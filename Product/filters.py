import django_filters
from ..OrderLine.models import OrderLine

class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = OrderLine
        fields = ['name']