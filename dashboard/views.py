from django.shortcuts import render


# Create your views here.


def home(request):
    return render(request, 'dashboard/dashboard.html')


def help(request):
    return render(request, 'dashboard/help.html')


def index(request):
    return render(request, 'index.html')
