from __future__ import annotations

import enum
from typing import List, Optional

from django.db import models


@enum.unique
class TerritoryCategory(models.TextChoices):
    region = 'O', 'Область або АРК'
    special = 'K', 'Місто, що має спеціальний статус'
    district = 'P', 'Район в області або в АРК'
    community = 'H', 'Територіальна громада'
    city = 'M', 'Місто'
    urban_village = 'T', 'Селище міського типу'
    village = 'C', 'Село'
    small_village = 'X', 'Селище'
    municipal_district = 'B', 'Район в місті'


class Territory(models.Model):
    class Meta:
        verbose_name_plural = "Territories"

    code = models.CharField(max_length=19, primary_key=True)
    name = models.CharField(max_length=1028)
    level = models.IntegerField()
    parent = models.ForeignKey(
        to='Territory',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    category = models.CharField(max_length=1, choices=TerritoryCategory.choices)
    children_count = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.code} - {self.name}'

    @staticmethod
    def get(code: str) -> Territory:
        return Territory.objects.get(code=code)

    @staticmethod
    def get_ancestors(code: Optional[str]) -> List[Territory]:
        if not code:
            return []

        territory = Territory.objects.filter(code=code).first()

        territories: List[Territory] = []
        while territory:
            territories.append(territory)
            territory = territory.parent
        return list(reversed(territories))

    @staticmethod
    def get_children(code: str) -> List[Territory]:
        return Territory.objects.filter(parent__code=code).all()

    @staticmethod
    def get_roots() -> List[Territory]:
        return Territory.objects.filter(level__exact=1).all()

    @staticmethod
    def get_by_search(query: Optional[str]) -> List[Territory]:
        if not query:
            return []
        territories = (
            Territory
            .objects
            .filter(
                models.Q(name__search=query) |
                models.Q(name__icontains=query) |
                models.Q(code__icontains=query)
            )
            .all()
        )
        return sorted(territories, key=lambda t: len(t.name))
