from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from datetime import date

from .models import Invoice
from .serializer import InvoiceSerializer

# Overview of APIs
@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'List of All Invoices':'invoices/',
        'Todays Invoices': 'today/',
        'Get By Date':'invoice/date',

    }
    return Response(api_urls)

# Get all invoices
@api_view(['GET'])
def invoice_list(request):
    invoices = Invoice.objects.all()
    serializer = InvoiceSerializer(invoices, many=True)
    return Response(serializer.data)

# Get today's invoices
@api_view(['GET'])
def get_latest_entries(request):
    today = date.today()
    print(today)
    invoices = Invoice.objects.filter(purchase_date__icontains=today)
    serializer = InvoiceSerializer(invoices, many=True)
    return Response(serializer.data)

# Get by date
@api_view(['GET'])
def get_by_date(request, date):
    invoices = Invoice.objects.filter(purchase_date__icontains=date)
    print(invoices)
    serializer = InvoiceSerializer(invoices, many=True)
    return Response(serializer.data)