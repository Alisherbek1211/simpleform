from django.shortcuts import redirect, render
from django.urls import reverse

from onlineshop.models import MinCategory, Product,Category
from .forms import *


# Create your views here.


def index(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    return render(request, "list.html", context)

def create(request):
    form = ProductForm()

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse("product-list"))

    context = {
        "form" : form
    }
    return render(request, "create.html", context)

def update(request, pk):
    product = Product.objects.filter(id=pk)
    if not product.exists():
        return redirect(reverse("product-list"))
    else:
        product = product.first()

    form = ProductForm(instance=product)

    if request.method == "POST":
        product = ProductForm(request.POST, request.FILES, instance=product)
        if product.is_valid():
            product.save()
            return redirect(reverse("product-list"))

    context = {
        "form": form
    }
    return render(request, "update.html", context)


def delete(request, pk):
    try:
        product = Product.objects.get(id=pk)
        product.delete()
    except Product.DoesNotExist:
        pass


    return redirect(reverse("product-list"))


def category_example_form(request):
    form = ProductForm()
    context = {
        "form" : form
    }
    return render(request, "example.html", context)