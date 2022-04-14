from django.shortcuts import render
from authapp.models import User
from django.contrib.auth.decorators import user_passes_test
from adminapp.forms import UserAdminRegisterForm, UserAdminProfileForm, CategoryAdminRegisterForm, ProductAdminProfileForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from mainapp.models import ProductCategories, Product

# Create your views here.
@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, "adminapp/admin.html")


@user_passes_test(lambda u: u.is_superuser)
def admin_users(request):
    context = {
        "title": "Админка | пользователи",
        "users": User.objects.all()
    }
    return render(request, "adminapp/admin-users-read.html", context)


@user_passes_test(lambda u: u.is_superuser)
def admin_user_create(request):
    if request.method == "POST":
        form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("adminapp:admin_users"))
        else:
            print(form.errors)
    else:
        form = UserAdminRegisterForm()


    context = {
        "title": "Админка | создать",
        "form": form
    }
    return render(request, "adminapp/admin-users-create.html", context)


@user_passes_test(lambda u: u.is_superuser)
def admin_user_update(request, id):
    user_select = User.objects.get(id=id)
    if request.method == "POST":
        form = UserAdminProfileForm(data=request.POST, instance=user_select, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("adminapp:admin_users"))
    else:
        form = UserAdminProfileForm(instance=user_select)

    context = {
        "title": "Админка | изменить пользователя",
        "form": form,
        "user_select": user_select
    }
    return render(request, "adminapp/admin-users-update-delete.html", context)


@user_passes_test(lambda u: u.is_superuser)
def admin_user_delete(request, id):
    user = User.objects.get(id=id)
    user.is_active = False
    user.save()
    return HttpResponseRedirect(reverse("adminapp:admin_users"))













@user_passes_test(lambda u: u.is_superuser)
def admin_categories(request):
    context = {
        "title": "Админка | товары",
        "categories": ProductCategories.objects.all()
    }
    return render(request, "adminapp/admin-categories-read.html", context)

@user_passes_test(lambda u: u.is_superuser)
def admin_categories_create(request):
    if request.method == "POST":
        form = CategoryAdminRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("adminapp:admin_categories"))
        else:
            print(form.errors)
    else:
        form = CategoryAdminRegisterForm()


    context = {
        "title": "Админка | создать",
        "form": form
    }
    return render(request, "adminapp/admin-categories-create.html", context)

@user_passes_test(lambda u: u.is_superuser)
def admin_category_update(request, id):
    category = ProductCategories.objects.get(id=id)
    if request.method == "POST":
        form = CategoryAdminRegisterForm(data=request.POST, instance=category, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("adminapp:admin_categories"))
    else:
        form = CategoryAdminRegisterForm(instance=category)

    context = {
        "title": "Админка | изменить пользователя",
        "form": form,
        "category": category
    }
    return render(request, "adminapp/admin-ctegories-update-delete.html", context)

@user_passes_test(lambda u: u.is_superuser)
def admin_category_delete(request, id):
    user = ProductCategories.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse("adminapp:admin_categories"))












@user_passes_test(lambda u: u.is_superuser)
def admin_products(request):
    context = {
        "title": "Админка | товары",
        "products": Product.objects.all()
    }
    return render(request, "adminapp/admin-product-read.html", context)


@user_passes_test(lambda u: u.is_superuser)
def admin_product_create(request):
    if request.method == "POST":
        form = ProductAdminProfileForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("adminapp:admin_products"))
        else:
            print(form.errors)
    else:
        form = ProductAdminProfileForm()


    context = {
        "title": "Админка | создать",
        "form": form
    }
    return render(request, "adminapp/admin-product-create.html", context)
@user_passes_test(lambda u: u.is_superuser)
def admin_product_update(request, id):
    product = Product.objects.get(id=id)
    if request.method == "POST":
        form = ProductAdminProfileForm(data=request.POST, instance=product, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("adminapp:admin_products"))
    else:
        form = ProductAdminProfileForm(instance=product)

    context = {
        "title": "Админка | изменить продукт",
        "form": form,
        "product": product
    }
    return render(request, "adminapp/admin-product-update-delete.html", context)


@user_passes_test(lambda u: u.is_superuser)
def admin_product_delete(request, id):
    user = Product.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse("adminapp:admin_products"))
