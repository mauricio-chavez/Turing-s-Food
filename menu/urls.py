"""Restaurants URL config"""

from django.urls import path

from . import views


urlpatterns = [
    path('', views.ItemListView.as_view(), name='items')
]
