import enum

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
