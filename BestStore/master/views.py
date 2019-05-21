from django.shortcuts import render


def home(request):
    return render(request, "master/homepage.html")


def register(request):
    return render(request, "master/register.html")


def render_login_form(request):
    return render(request, 'master/login.html')