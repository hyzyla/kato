from django.http import HttpRequest
from rest_framework.renderers import BrowsableAPIRenderer
from rest_framework.views import APIView
from rest_framework_api_key.permissions import HasAPIKey


class TerritoryAPIPermission(HasAPIKey):
    message = (
        'Відмовлено у доступі до API. Для отримання доступу напишіть мені '
        'на електронну пошту hyzyla@gmail.com чи в телеграм https://t.me/hyzyla'
    )

    def has_permission(self, request: HttpRequest, view: APIView) -> bool:

        # always allow to perform request when browsable api rendered is selected
        renderer = getattr(request, 'accepted_renderer', None)
        if isinstance(renderer, BrowsableAPIRenderer):
            return True

        # in other cases verify API token
        return super().has_permission(request, view)
