import django_filters
from apps.product.models import Product, ProductCategory
from django.db.models import Q
from django.shortcuts import get_object_or_404


class ProductFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', method='filter_title')
    price_min = django_filters.NumberFilter(field_name="price", lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name="price", lookup_expr='lte')

    def filter_title(self, queryset, name, value):
        # print(len(queryset))
        search_term = value
        queryset = queryset.filter(
            Q(title__icontains=search_term) |
            Q(description__icontains=search_term)
        )
        print('title')
        return queryset

    class Meta:
        model = Product
        fields = ['title', 'price_min', 'price_max', 'category']
