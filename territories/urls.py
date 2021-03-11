from django.urls import path

from territories import views

urlpatterns = [
    path('', views.index)
]
