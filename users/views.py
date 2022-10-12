from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .forms import UserLoginForm, UserRegisterForm, UserProfileForm
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required


def login(request):
    """Авторизация"""
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('homepage'))
    else:  # request.method != 'POST'
        form = UserLoginForm()
    return render(request, 'auth/login.html', context={'form': form})


def register(request):
    """Регистрация"""
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались!')
            return HttpResponseRedirect(reverse('login'))
    else:
        form = UserRegisterForm()

    return render(request, 'auth/register.html', context={'form': form})


@login_required
def account_user(request):
    """Личный кабинет"""
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, files=request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('profile'))
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'auth/profile.html', context={'form': form})


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('homepage'))
