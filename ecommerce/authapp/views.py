from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def login_user(request):
    return render(request, 'templates/auth/login.html', {})

def register_user(request):
    return render(request, 'templates/auth/register.html', {})