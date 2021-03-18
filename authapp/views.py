from django.conf import settings
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from authapp.forms import ShopUserLoginForm, ShopUserRegisterForm, ShopUserProfileForm
from basketapp.models import Basket


def login(request):
    title = 'Вход'

    if request.method == 'POST':
        login_form = ShopUserLoginForm(data=request.POST)
        if login_form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main'))
        else:
            print(login_form.errors)
    else:
        login_form = ShopUserLoginForm()

    content = {'title': title, 'login_form': login_form}
    return render(request, 'authapp/login.html', content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))


def register(request):
    title = 'Регистрация'

    if request.method == "POST":
        register_form = ShopUserRegisterForm(request.POST, request.FILES)
        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        register_form = ShopUserRegisterForm()
    content = {'title': title, 'register_form': register_form}
    return render(request, 'authapp/register.html', content)


@login_required
def profile(request):
    title = 'Профиль'
    user = request.user
    if request.method == 'POST':
        profile_form = ShopUserProfileForm(
            request.POST, request.FILES, instance=user)
        if profile_form.is_valid():
            profile_form.save()
            return HttpResponseRedirect(reverse('auth:profile'))
    else:
        profile_form = ShopUserProfileForm(instance=user)
        basket = Basket.objects.filter(user=user)
        content = {
            'title': title,
            'profile_form': profile_form,
            'basket': basket,
            'media_url': settings.MEDIA_URL}
        return render(request, 'authapp/profile.html', content)
