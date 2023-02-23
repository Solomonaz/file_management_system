from django.shortcuts import render


def login(request):
    return render(request, 'accounts/login.html')


def sign_up(request):
    return render(request, 'accounts/sign_up.html')

def user_list(request):
    return render(request, 'accounts/user_list.html')

def new_user(request):
    return render(request, 'accounts/new_user.html')