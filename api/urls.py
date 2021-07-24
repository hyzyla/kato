from rest_framework import routers

from territories import views as territories

router = routers.SimpleRouter()
router.register('territories', territories.TerritoryViewSet)

urlpatterns = router.urls
