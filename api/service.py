from django_filters import rest_framework as filters
import django_filters

from api.models import Advert


class AdvertFilterSet(filters.FilterSet):
    created_start = django_filters.DateFilter(field_name='created', lookup_expr='gte')
    created_end = django_filters.DateFilter(field_name='created', lookup_expr='lte')

    class Meta:
        model = Advert
        fields = ['created_start', 'created_end']
