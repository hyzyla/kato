from rest_framework import serializers

from territories.models import Territory


class TerritorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Territory
        fields = [
            'code',
            'name',
            'level',
            'parent_id',
            'parent',
            'category',
            'children_count',
        ]
