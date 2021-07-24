from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, exceptions
from rest_framework.negotiation import DefaultContentNegotiation

from territories.filters import TerritoryViewSetFilter
from territories.models import Territory
from territories.permissions import HasAPIKeyJSON
from territories.serializers import TerritorySerializer


def index(request):
    territories = Territory.get_roots()
    context = {'territories': territories}
    return render(request, 'territories/index.html', context)


def search(request):
    query = request.GET.get('q')
    territories = Territory.get_by_search(query=query)
    context = {'territories': territories}
    return render(request, 'territories/search.html', context)


def details(request, code: str):
    territory = Territory.get(code=code)
    children = Territory.get_children(code=code)
    context = {'territory': territory, 'children': children, 'parent': territory.parent}
    return render(request, 'territories/details.html', context)


class TerritoryViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [HasAPIKeyJSON]
    queryset = Territory.objects.order_by('code').all()
    serializer_class = TerritorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TerritoryViewSetFilter
