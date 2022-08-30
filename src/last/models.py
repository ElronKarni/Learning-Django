from django.db import models

# Create your models here.

class Last(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(max_length=120)
    price = models.DecimalField(max_digits=1000, decimal_places=2)