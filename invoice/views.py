from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView
from django.db.models import Sum

from datetime import date
import datetime

from .models import Invoice, Expense
from .forms import AddItemForm, AddExpenseForm


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
        context['expenses']= Expense.objects.filter(expense_date__icontains=today)
        context['amount'] = Invoice.objects.filter(purchase_date__icontains=today).aggregate(amount = Sum('selling_price'))['amount']
        return context


class AddNewItem(CreateView):
    model = Invoice
    form_class = AddItemForm
    # template_name = 'invoice/add_new_item.html'
    template_name = 'invoice/index.html'

    def get_success_url(self):
        return '/'


class AddNewExpense(CreateView):
    model = Expense
    form_class = AddExpenseForm
    template_name = 'invoice/add_new_expense.html'

    def get_success_url(self):
        return '/'


# Function used to get the data based on the entered date
def get_by_date(request):
    if request.method == 'POST':
        
        # query contains the date entered by the user
        query = request.POST['search_by_date']
        if query:
<<<<<<< HEAD
            query_result = Invoice.objects.filter(purchase_date__icontains=query)
            query_result2 = Expense.objects.filter(expense_date__icontains=query)
=======
            invoice_by_date = Invoice.objects.filter(purchase_date__icontains=query)
            expense_by_date = Expense.objects.filter(expense_date__icontains=query)

>>>>>>> new_feature
            # Summing the selling price by the date
            amount = Invoice.objects.filter(purchase_date__icontains=query).aggregate(amount = Sum('selling_price'))['amount']

            if invoice_by_date:
                # Changing Format of Input Date to Display in Template
                query = datetime.datetime.strptime(query, '%Y-%m-%d').strftime('%d-%B-%Y')
<<<<<<< HEAD
                context = {
                    'query_result':query_result,
                    'query_date':query,
                    'amount': amount,
                    'query_result2': query_result2,
                }
                print(context)
                return render(request, 'invoice/get_by_date.html', context)
            else:
                return render(request, 'invoice/get_by_date.html')
=======

                return render(request, 'invoice/get_by_date.html', 
                {   'query_result':invoice_by_date,
                    'query_date':query,
                    'amount': amount,
                    'query_result2': expense_by_date,
                })
            else:
                return render(request, 'invoice/get_by_date.html')
        else:
            return HttpResponse('No Data Found!')
    else:
        return HttpResponse('No Data Found!')

>>>>>>> new_feature
