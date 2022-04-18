from django.shortcuts import render
from authapp.models import User
from django.contrib.auth.decorators import user_passes_test
from adminapp.forms import UserAdminRegisterForm, UserAdminProfileForm, CategoryAdminRegisterForm, ProductAdminProfileForm
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from mainapp.models import ProductCategories, Product
from django.core.paginator import Paginator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from adminapp.mixin import BaseClassContextMixin, ContextMixin, CustomDispatchMixin

# Create your views here.
class IndexTemlateView(TemplateView, BaseClassContextMixin, CustomDispatchMixin):
    template_name = "adminapp/admin.html"
    title = "главная страница"


class UserListView(ListView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    template_name = "adminapp/admin-users-read.html"
    title = "Пользователи"
    context_object_name = "users"


class UserCreateView(CreateView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    template_name = "adminapp/admin-users-create.html"
    form_class = UserAdminRegisterForm
    title = "создать пользователя"
    success_url = reverse_lazy("adminapp:admin_users")

class UserUpdateView(UpdateView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    template_name = "adminapp/admin-users-update-delete.html"
    form_class = UserAdminProfileForm
    title = " изменить"
    success_url = reverse_lazy("adminapp:admin_users")


class UserDeleteViewView(DeleteView, CustomDispatchMixin):
    model = User
    template_name = "adminapp/admin-users-update-delete.html"
    form_class = UserAdminProfileForm
    title = " изменить"
    success_url = reverse_lazy("adminapp:admin_users")

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

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
