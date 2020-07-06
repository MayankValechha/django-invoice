from django import forms
from .models import Invoice


class AddItemForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['product_name', 'cost_price', 'selling_price']
        widgets = {
            'product_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Product Name...'}),
            'cost_price': forms.TextInput(attrs={'class':'form-control'}),
            'selling_price': forms.TextInput(attrs={'class':'form-control'}),
        }