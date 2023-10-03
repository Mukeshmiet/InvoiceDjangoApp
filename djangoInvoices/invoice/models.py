from django.db import models

class Invoice(models.Model):
    Date = models.DateField()
    InvoiceCustomerName = models.CharField(max_length=255)
    objects = models.Manager() 

class InvoiceDetail(models.Model):
    invoice = models.ForeignKey(Invoice, related_name='details', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    objects = models.Manager() 
