from territories import views as territories

from rest_framework import routers
from django.utils.safestring import mark_safe


class TerritoryAPIRootView(routers.APIRootView):
    """
    Controls appearance of the API root view
    """

    def get_view_name(self) -> str:
        return "API"

    def get_view_description(self, html=False) -> str:
        text = "API отримання списку КАТОТТГ"
        if html:
            return mark_safe(f"<p>{text}</p>")
        else:
            return text


class TerritoriesRouter(routers.DefaultRouter):
    APIRootView = TerritoryAPIRootView


router = TerritoriesRouter()
router.register('territories', territories.TerritoryViewSet)

urlpatterns = router.urls
