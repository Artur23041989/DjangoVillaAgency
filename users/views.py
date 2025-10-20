from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages



def login_user(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except ObjectDoesNotExist:
            messages.error(request, "Username not found")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('all_properties')
        else:
            messages.error(request,"Username or password is incorrect")

    return render(request, 'users/login_register.html')


def logout_user(request):
    logout(request)
    messages.error(request, "User was logout")
    return redirect('index')


def register_user(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, "User account was created!!")
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Error registration")

    context = {
        'page': page,
        'form': form
    }
    return render(request, 'users/login_register.html', context)