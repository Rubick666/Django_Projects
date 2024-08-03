from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm, Product
from django.http import HttpResponse


# Create your views here.


def product_list(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'index2.html', {'product': product})

def edit_product(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'edit.html', {'form': form})
    
def delete_product(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == "POST":
        product.delete()
        return redirect('product_list')
    return render(request, 'delete.html', {'product': product})

def home(request):
    return HttpResponse("Hello world !")