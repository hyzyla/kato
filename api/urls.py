from territories import views as territories

from rest_framework import routers

router = routers.DefaultRouter()
router.register('territories', territories.TerritoryViewSet)

urlpatterns = router.urls
