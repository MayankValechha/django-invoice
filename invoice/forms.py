from django import forms
from .models import Invoice


class AddItemForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['product_name', 'cost_price', 'selling_price']
        widgets = {
            'product_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Product Name...'}),
            'cost_price': forms.TextInput(attrs={'class':'form-control', 'placeholder':' Cost Price...'}),
            'selling_price': forms.TextInput(attrs={'class':'form-control', 'placeholder':' Selling Price...'}),
        }
