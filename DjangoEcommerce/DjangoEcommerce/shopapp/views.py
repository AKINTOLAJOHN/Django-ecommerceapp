from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import Product
from django.contrib.auth.models import User
from django.db import transaction
from django.contrib import messages
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect
from .forms import Product_Form
import json

# Create your views here.
def productView(request):
    """
    to send the form to add product and insert in the database 
    """
    if request.method == 'POST':
        form = Product_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            form = Product_Form(request.POST, request.FILES)
        return render(request, 'shopapp/shop.html',{
            'form' : form
        })
    else:
        form = Product_Form(request.POST, request.FILES)
        return render(request, 'shopapp/addproduct.html',{
            'form': form
    })

def approve(request):
    """
    to loop through the database and send all the item to the viewproduct so admin can see the item which the staff add 
    """
    productItem = Product.objects.all()
    return render(request, 'shopapp/viewproduct.html', {'productItem': productItem })

def products(request):
    """
    to loop through the database and send all the item in the shop to the font end
    """
    products = Product.objects.all()
    return render(request, 'shopapp/shop.html', {'products':products})


def viewInDetail(request, product_id):
    """
    to loop through the database and send the item at the index of product id 
    """
    viewGood = Product.objects.all().filter(id=product_id)
    print(viewGood)
    return render(request, 'shopapp/viewInDetails.html', {'viewGood': viewGood})    
 
def addToCart(request, product_id):
    data = json.loads(request.body)
    print(data)
    return products(request)    


        


def cart(request):
    products = Product.objects.all()
    return render(request, 'shopapp/cart.html', {'products': products})

# def checkout(request):
#     products = Product.objects.all()
#     return render(request, 'shopapp/checkout', {'products':products})

    


@login_required
def deapproval(request, product_id):
    """
    for the superuser to be able to approval item that can be see by the customer 
    """
    goods = Product.objects.get(id = product_id)
    if goods.item_validation:
        goods.item_validation = 0
    else:
        goods.item_validation = 1
    goods.save()
    return approve(request)