from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView
from django.db.models import Sum

from datetime import date
import datetime

from . models import Invoice
from .forms import AddItemForm


class ListSoldItems(ListView):
    model = Invoice
    template_name = 'invoice/index.html'
    ordering = ['-purchase_date']
    

class GetLatestSoldItems(ListView):
    today = date.today()
    queryset = Invoice.objects.filter(
        purchase_date__year=today.year,
        purchase_date__month=today.month,
        purchase_date__day=today.day
    )
    template_name = 'invoice/get_latest_item.html'

    def get_context_data (self, today=today):
        context = super().get_context_data(today=today)
        context['amount'] = Invoice.objects.filter(purchase_date__icontains=today).aggregate(amount = Sum('selling_price'))['amount']
        return context


class AddNewItem(CreateView):
    model = Invoice
    form_class = AddItemForm
    # template_name = 'invoice/add_new_item.html'
    template_name = 'invoice/index.html'

    def get_success_url(self):
        return '/'


# Function used to get the data based on the entered date
def get_by_date(request):
    if request.method == 'POST':
        
        # query contains the date entered by the user
        query = request.POST['search_by_date']
        if query:
            query_result = Invoice.objects.filter(purchase_date__icontains=query)
            
            # Summing the selling price by the date
            amount = Invoice.objects.filter(purchase_date__icontains=query).aggregate(amount = Sum('selling_price'))['amount']

            if query_result:
                # Changing Format of Input Date to Display in Template
                query = datetime.datetime.strptime(query, '%Y-%m-%d').strftime('%d-%B-%Y')

                return render(request, 'invoice/get_by_date.html', 
                {   'query_result':query_result,
                    'query_date':query,
                    'amount': amount
                })
            else:
                return render(request, 'invoice/get_by_date.html')