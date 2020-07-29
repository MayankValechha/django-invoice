from django.contrib import admin
from .models import Invoice, Expense
# Register your models here.

admin.site.register(Invoice)
admin.site.register(Expense)
