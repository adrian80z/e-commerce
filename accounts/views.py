from django.shortcuts import render, redirect, reverse
from django.contrib import auth

# Create your views here.


def index(request):
    """Return index.html file"""
    return render(request, 'index.html')


def logout(request):
    """Logout user"""
    auth.logout(request)
    return redirect(reverse('index'))
