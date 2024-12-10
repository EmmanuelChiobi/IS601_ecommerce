from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm

# Create your views here.
def login_user(request):
    return render(request, 'auth/login.html', {})

def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = UserRegistrationForm()

    return render(request, 'auth/register.html', {'form': form})

@login_required
def shop_redirect(request):
    return render(request, 'products.html')