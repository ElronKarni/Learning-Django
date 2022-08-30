from django.db import models
from django.urls import reverse
# Create your models here.
class Cart(models.Model):
    item_name = models.CharField(max_length=120)
    item_description = models.TextField(max_length=120)
    item_price = models.DecimalField( decimal_places=2, max_digits=100000)

    def get_absolute_url(self):
        return reverse("cart-delete", kwargs={'id': self.id}) #f"/cart/{self.id}/"
