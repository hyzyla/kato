from django.urls import path

from territories import views

urlpatterns = [
    path('', views.index, name='territories'),
    path('territories/search', views.search, name='territories-search'),
    path('territories/<code>', views.details, name='territory'),
]
