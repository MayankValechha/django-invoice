from django.contrib import admin
from django.urls import path
from . views import ListSoldItems, GetLatestSoldItems, AddNewItem, get_by_date


urlpatterns = [
    path('', ListSoldItems.as_view(), name='home'),
    path('today/', GetLatestSoldItems.as_view(), name='latest_items'),
    path('add_item/', AddNewItem.as_view(success_url="/"), name='add_item'),
    path('search/', get_by_date, name='search'),
]