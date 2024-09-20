from django.shortcuts import render


def login(request):
    return render(request, 'myapp/login.html')


def signup(request):
    return render(request, 'myapp/signup.html')


def dashboard(request):
    return render(request, 'myapp/dashboard.html')
