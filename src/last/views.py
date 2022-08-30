from multiprocessing import context
from django.shortcuts import render
from .forms import lastForm
from .models import Last
# Create your views here.

def last_create(request):
    queryset = Last.objects.all()
    form = lastForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = lastForm()
    context = {
        'object_list': queryset,
        'form': form,
    }

    return render(request, 'last/create.html', context)