from django.shortcuts import render
from mainapp.models import Product, ProductCategories

def index(request):
  context = {
    "title_logo": "GeekShop",
    "title": "GeekShop Store"
  }
  return render(request, "mainapp/index.html", context=context)

def products(request):
    context = {
        "title_logo": "GeekShop",
        "title": "GeekShop - Каталог",
        "categories": ProductCategories.objects.all(),
        "products": Product.objects.all()
    }
    return render(request, "mainapp/products.html", context=context)
