from django.urls import path

from territories import views

urlpatterns = [
    path('', views.index, name='territories'),
    path('search', views.search, name='territories-search'),
    path('<code>', views.details, name='territory'),
]
