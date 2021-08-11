from django.http import HttpResponse
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer

from territories.filters import TerritoryViewSetFilter
from territories.models import Territory
from territories.pagination import TerritoryPagination
from territories.permission import TerritoryAPIPermission
from territories.serializers import TerritorySerializer


def index(request):
    territories = Territory.get_roots()
    context = {'territories': territories}
    return render(request, 'territories/index.html', context)


def ads(request):
    return HttpResponse('google.com, pub-4422566096376436, DIRECT, f08c47fec0942fa0')


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
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    permission_classes = [TerritoryAPIPermission]
    authentication_classes = []
    queryset = Territory.objects.order_by('code').all()
    serializer_class = TerritorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TerritoryViewSetFilter
    pagination_class = TerritoryPagination
