from django.shortcuts import render, redirect
# from django.contrib.auth import login
from .forms import Register
from django.contrib import messages
from accounts.models import Account
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

def login(request):

    return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        register_form = Register(request.POST)
        if register_form.is_valid():
            email = register_form.cleaned_data['email']
            password = register_form.cleaned_data['password']
            username = register_form.cleaned_data['username']
            user = Account.objects.create_user(email=email, username=username, password=password)
            user.save()
            messages.success(request, 'Registration successful!')
            return redirect('login')
    else:
        register_form = Register()
    context = {
        'register_form':register_form
    }

    return render(request, 'accounts/register.html', context)

def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)

            return redirect('index')
        else:
            messages.error(request, "Invalid login credentials!")
            return redirect('login')

    return render(request, 'accounts/login.html')

@login_required(login_url='login')
def logout(request):
    messages.success(request, 'you are logged out!')
    auth.logout(request)
    return redirect('login')