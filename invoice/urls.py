from django.contrib import admin
from django.urls import path
from . views import ListSoldItems, GetLatestSoldItems, AddNewItem, get_by_date


urlpatterns = [
    path('', AddNewItem.as_view(), name='home'),
    path('today/', GetLatestSoldItems.as_view(), name='today'),
    path('search/', get_by_date, name='search'),
]