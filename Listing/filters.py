from django_filters import rest_framework as filters
from .models import Job

class JobFilter(filters.FilterSet):
    price_min = filters.NumberFilter(field_name="price", lookup_expr='gte')
    price_max = filters.NumberFilter(field_name="price", lookup_expr='lte')
    # borough = filters.CharFilter(field_name="borough", lookup_expr='iexact')
    borough = filters.CharFilter(field_name="borough", lookup_expr='icontains')
    title = filters.CharFilter(field_name="title", lookup_expr='icontains')
    class Meta:
        model = Job
        fields = ['price_min', 'price_max', 'borough', 'title']