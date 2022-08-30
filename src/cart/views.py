from multiprocessing import context
from django.shortcuts import render, get_object_or_404, redirect
from .models import Cart
from .form import CartForm
# Create your views here.

def cart_view(request, id):
    queryset = Cart.objects.all()
    obj = get_object_or_404(Cart, id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('../../../')
    context = {
        'object_list': queryset,
        'object': obj,
    }
    return render(request, "cart/cart_delete.html",context)

