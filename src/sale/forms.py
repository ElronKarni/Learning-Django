from faulthandler import disable
from django import forms

from .models import Sale
class SaleForm(forms.ModelForm):
    product_name = forms.CharField(max_length=100)
    product_description = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'item description'}))
    product_discount = forms.CharField(disabled=True)
    product_price = forms.DecimalField(max_digits=100000, decimal_places=2)
    class Meta:
        model = Sale
        fields = [
            'product_name',
            'product_description',
            'product_discount',
            'product_price',
        ]

def discount_check(self, *args, **kwargs):
    productName = self.cleaned_data.get('product_name')
    productDiscount = self.cleaned_data.get('product_discount')
    if 'blue shirt' in productName:
        return productDiscount + 3
    else:
        return forms.CharField(initial=20,disabled=True)
