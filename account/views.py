from django.shortcuts import render

# Create your views here.
from .models import *
from .forms import *


def Account(request):
    customer = request.user
    form = CustomerForm(instance=customer)

    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()

    context = {'form':form}

    return render(request, 'account/account.html', context)