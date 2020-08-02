from django import forms
from .models import Invoice, Expense


class AddItemForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['product_name', 'cost_price', 'selling_price']
        widgets = {
            'product_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Product Name...'}),
            'cost_price': forms.TextInput(attrs={'class':'form-control', 'placeholder':' Cost Price...'}),
            'selling_price': forms.TextInput(attrs={'class':'form-control', 'placeholder':' Selling Price...'}),
        }


class AddExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['expense_name', 'expense_amount']
        widgets = {
            'expense_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':' Expense Item...'}),
            'expense_amount': forms.TextInput(attrs={'class':'form-control', 'placeholder':' Expense Price...'}),
        }
