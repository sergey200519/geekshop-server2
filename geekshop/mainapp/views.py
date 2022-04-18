from django.shortcuts import render
from mainapp.models import Product, ProductCategories
from django.core.paginator import Paginator

def index(request):
  context = {
    "title_logo": "GeekShop",
    "title": "GeekShop Store"
  }
  return render(request, "mainapp/index.html", context=context)

def products(request, id_category=None, page=1):
    if id_category:
        category = ProductCategories.objects.filter(id=id_category)
        product = Product.objects.filter(category=id_category)
    else:
        category = ProductCategories.objects.all()
        product = Product.objects.all()

    pagination = Paginator(product, per_page=2)

    product_pagination = pagination.page(page)
    # except PageNotAnInteger:
    #     product_pagination = pagination.page(1)


    context = {
        "title_logo": "GeekShop",
        "title": "GeekShop - Каталог",
        "categories": category,
        "products": product_pagination
    }
    return render(request, "mainapp/products.html", context=context)


def all_products(request):

    context = {
        "title_logo": "GeekShop",
        "title": "GeekShop - Каталог",
        "categories": ProductCategories.objects.all(),
        "products": Product.objects.all()
    }
    return render(request, "mainapp/products.html", context=context)
