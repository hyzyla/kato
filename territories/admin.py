from django.contrib import admin

from territories import models


class TerritoryAdmin(admin.ModelAdmin):
    raw_id_fields = ["parent"]


admin.site.register(models.Territory, TerritoryAdmin)
