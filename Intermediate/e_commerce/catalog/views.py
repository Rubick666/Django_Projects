from django.shortcuts import render, redirect
from .models import Product, CartItem
from django.http import HttpResponse

# Create your views here.

def product_list(request):
    products = Product.objects.all()
    return render(request, "index.html", {'products': products})

def product_detail(request, pk):
    product = Product.objects.get(pk = pk)
    return render(request, "index2.html", {'product': product})

def home(request):
    return HttpResponse("Hello, Welcome to my shopping site")

def view_cart(request):
    cart_items = CartItem.objects.filter(user = request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

def add_to_cart(request, id):
    product = Product.objects.get(id=id)
    cart_item = CartItem.objects.get_or_create(product=product, user = request.user)
    cart_item.quantitiy += 1
    cart_item.save()
    return redirect('view_cart')

def remove_from_cart(request, id):
    cart_item = CartItem.objects.get(id = id)
    cart_item.delete()
    return redirect('view_cart')