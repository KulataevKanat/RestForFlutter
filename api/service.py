from django_filters import rest_framework as filters
import django_filters

from api.models import Announcement


class AnnouncementFilterSet(filters.FilterSet):
    created_start = django_filters.DateFilter(field_name='created', lookup_expr='gte')
    created_end = django_filters.DateFilter(field_name='created', lookup_expr='lte')

    class Meta:
        model = Announcement
        fields = ['created_start', 'created_end']
