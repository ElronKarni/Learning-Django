from django import forms
from .models import Last
class lastForm(forms.ModelForm):
    title = forms.CharField(max_length=120)
    description = forms.CharField(max_length=120)
    price = forms.DecimalField(max_digits=1000, decimal_places=2)
    class Meta:
        model = Last
        fields = {
            'title',
            'description',
            'price',
        }