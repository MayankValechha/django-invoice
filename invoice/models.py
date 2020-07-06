from django.db import models
from django.db.models import Sum


""" class InvoiceManager(models.Manager):
    def get_total(self):
        return self.aggregate(amount = Sum('selling_price'))['amount'] """


class Invoice(models.Model):
    product_name = models.CharField(max_length=255)
    purchase_date = models.DateTimeField(auto_now=True)
    cost_price = models.IntegerField()
    selling_price = models.IntegerField()

    # objects = InvoiceManager()

    def __str__(self):
        return f'{self.product_name} added.'

    # @property
    # def get_total(self):
    #     amount = Invoice.objects.aggregate(amount = Sum('selling_price'))['amount']
    #     return amount