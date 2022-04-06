from django.shortcuts import render
from authapp.forms import UserLoginForm, UserRegisterForm
from django.contrib import auth, messages
# from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.urls import reverse
# from django.contrib.messages import middleware

# Create your views here.

def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            if user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()

    context = {
        "title": "Geekshop |  Авиоризация",
        "form": form
    }
    return render(request, "authapp/login.html", context)





def register(request):
    if request.method == "POST":
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Вы успешно зарегистрировалилсь")
            return HttpResponseRedirect(reverse('authapp:login'))
        else:
            print(form.errors)
    else:
        form = UserRegisterForm()
    context = {
        "title": "Geekshop |  Регистрация",
        "form": form
    }
    return render(request, "authapp/register.html", context)





def logout(request):
    auth.logout(request)
    return render(request, "mainapp/index.html")
