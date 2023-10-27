from django.shortcuts import render
import random
from .models import *
# Create your views here.


def home(request):
    Product.objects.create(name=f"Product-{random.randint(1,100)}", price=100)
    return render(request, 'index.html')
