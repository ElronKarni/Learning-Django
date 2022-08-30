from re import L
from django.shortcuts import render
from .forms import SaleForm
from .models import Sale
# Create your views here.

def sale_create_view(request):
    initial_data = {
        'product_discount':'10%'
    }
    
    queryset = Sale.objects.all()
    form = SaleForm(request.POST or None, initial=initial_data)
    if form.is_valid():
        form.save()
        form = SaleForm()
    context = {
        'form': form,
        'sale_list': queryset
    }
    
    return render(request, 'sale/create.html', context)