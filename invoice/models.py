from django.db import models


class Invoice(models.Model):
    product_name = models.CharField(max_length=255)
    purchase_date = models.DateTimeField(auto_now=True)
    cost_price = models.IntegerField()
    selling_price = models.IntegerField()

    def __str__(self):
        return f'{self.product_name} added.'


class Expense(models.Model):
    expense_name = models.CharField(max_length=255)
    expense_amount = models.IntegerField()
    expense_date = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return f'{self.expense_name} added.'