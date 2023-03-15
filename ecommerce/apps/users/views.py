from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import NewUserForm


def signUp(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Тіркелу сәтті өтті!")
            return redirect("users:loginPage")
        messages.error(request, "Тіркелу барысында қателіктер пайда болды")
    else:
        form = NewUserForm()
    return render(request, "users/sign-up.html", {
        'form': form
    })


def loginPage(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Қош келдіңіз, {username}!")
                return redirect("catalog:homePage")
            else:
                messages.error(request, "Логин немесе пароль қате.")
        else:
            messages.error(request, "Логин немесе пароль қате.")
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", {
        'form': form
    })


def logoutUser(request):
    logout(request)
    messages.info(request, "Сіз платформадан сәтті шықтыңыз.")
    return redirect("catalog:homePage")