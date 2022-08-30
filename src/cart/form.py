from django import forms
from .models import Cart


class CartForm(forms.ModelForm):
    item_name = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'Item Name'}))
    item_description = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Item Description', 'cols':100,'rows':20}))
    item_price = forms.DecimalField()
    class Meta:
        model = Cart
        fields = [
            'item_name',
            'item_description',
            'item_price',
        ]
            

        