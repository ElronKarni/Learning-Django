from django.db import models

# Create your models here.
class Sale(models.Model):
    product_name = models.CharField(max_length=100)
    product_description = models.TextField(max_length=300)
    product_discount = models.CharField(max_length=10)
    product_price = models.DecimalField(max_digits=100000, decimal_places=2)
  