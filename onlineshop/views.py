from onlineshop.models import MinCategory, Product,Category
from django.shortcuts import redirect, render
from django.urls import reverse
# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    return render(request, "list.html", context)

def create(request):
    if request.method == "POST":
        name = request.POST.get("name", None)
        content = request.POST.get("content", None)
        image = request.POST.get("image", None)
        stock = request.POST.get("stock", None)
        category_id = request.POST.get("category_id", None)
        price = request.POST.get("price", None)
        rating = request.POST.get("rating", None)

        category = MinCategory.objects.get(id=category_id)

        p = Product()
        p.name = name
        p.content = content
        p.image = image
        p.stock = stock
        p.category = category
        p.price = price
        p.rating = rating
        p.save()

        return redirect(reverse("product-list"))
    categories = Category.objects.all()
    context = {
        "categories": categories
    }
    return render(request, "create.html", context)

def update(request, pk):
    product = Product.objects.filter(id=pk)
    if not product.exists():
        return redirect(reverse("product-list"))
    else:
        product = product.first()
    if request.POST:
        title = request.POST.get("title", None)
        content = request.POST.get("title", None)
        image = request.POST.get("image", None)
        stock = request.POST.get("stock", None)
        category_id = request.POST.get("category_id", None)
        price = request.POST.get("price", None)
        rating = request.POST.get("rating", None)

        category = MinCategory.objects.get(id=category_id)

        product.title = title
        product.content = content
        product.image = image
        product.stock = stock
        product.category = category
        product.price = price
        product.rating = rating
        product.save()

        return redirect(reverse("product-list"))
    categories = Category.objects.all()
    context = {
        "categories": categories,
        "product": product 
    }
    return render(request, "update.html", context)


def delete(request, pk):
    try:
        product = Product.objects.get(id=pk)
        product.delete()
    except Product.DoesNotExist:
        pass


    return redirect(reverse("product-list"))