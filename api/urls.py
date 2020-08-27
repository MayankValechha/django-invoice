from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name='overview'),   
    path('invoices/', views.invoice_list, name='invoice_list'), 
]
