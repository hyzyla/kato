import django_filters
from django.db import models
from django_filters.rest_framework import FilterSet

from territories.models import Territory


class TerritoryViewSetFilter(FilterSet):
    class Meta:
        model = Territory
        fields = ['code', 'name', 'level', 'parent', 'category']
        filter_overrides = {
            models.ForeignKey: {
                'filter_class': django_filters.CharFilter,
            },
        }
