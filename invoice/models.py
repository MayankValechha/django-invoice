from django.db import models
from django.db.models import Sum


class Invoice(models.Model):
    product_name = models.CharField(max_length=255)
    purchase_date = models.DateTimeField(auto_now=True)
    cost_price = models.IntegerField()
    selling_price = models.IntegerField()

    def __str__(self):
        return f'{self.product_name} added.'