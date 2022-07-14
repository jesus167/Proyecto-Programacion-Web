import json
from random import random
from django.shortcuts import render
from .models import Order, OrderDetail
from Tienda.models import Producto
# Create your views here.


def seguimiento(request):
    

    return render(request, "seguimiento/tracking.html")