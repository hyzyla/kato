from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from territories.filters import TerritoryViewSetFilter
from territories.models import Territory
from territories.serializers import TerritorySerializer


def index(request):
    territories = Territory.objects.filter(level__exact=1).all()
    context = {'territories': territories}
    return render(request, 'territories/index.html', context)


class TerritoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Territory.objects.order_by('code').all()
    serializer_class = TerritorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TerritoryViewSetFilter

    def get_queryset(self):
        queryset = self.queryset
        return queryset
