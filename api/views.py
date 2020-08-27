from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Invoice

from .serializer import InvoiceSerializer
# Create your views here.

@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'List':'/task_view',
        'Detail View': '/task-detail/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def invoice_list(request):
    invoices = Invoice.objects.all()
    serializer = InvoiceSerializer(invoices, many=True)
    return Response(serializer.data)