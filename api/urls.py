from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name='overview'),   
    path('invoices/', views.invoice_list, name='invoice_list'), 
    path('today/', views.get_latest_entries, name='latest_entry'), 
    path('invoice/<str:date>/', views.get_by_date),
]
