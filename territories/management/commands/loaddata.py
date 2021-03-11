import argparse
from itertools import islice

from django.core.management.base import BaseCommand, CommandError
from django.db import connection

from territories.models import Territory, TerritoryCategory
import openpyxl


class Command(BaseCommand):
    help = 'Load data from XLSX to database'

    def add_arguments(self, parser):
        parser.add_argument(
            'file',
            metavar='FILE',
            nargs=1,
            help='Input XLSX file',
            type=argparse.FileType('rb'),
        )

    def handle(self, *args, **options):

        file = options['file'][0]
        workbook = openpyxl.load_workbook(file)
        sheet = workbook.active
        for row in islice(sheet.rows, 3, None):
            if not row or row[0].value is None:
                break
            *levels_cells, category_cell, name_cell = row
            name = name_cell.value
            category = category_cell.value
            levels = [cell.value for cell in levels_cells if cell.value]
            code = levels[-1]
            parent = levels[-2] if len(levels) > 1 else None
            territory = Territory(
                code=code,
                name=name,
                parent_id=parent,
                level=len(levels),
                category=TerritoryCategory(category)
            )
            territory.save()
            print(territory)

        with connection.cursor() as cursor:
            cursor.execute('''
                UPDATE territories_territory
                SET children_count = coalesce((
                    SELECT count(t.code) as cnt
                    FROM territories_territory t
                    WHERE t.parent_id IS NOT NULL
                        AND territories_territory.code = t.parent_id
                    GROUP by t.parent_id), 0)
            ''')

        print('Successfully load data')
