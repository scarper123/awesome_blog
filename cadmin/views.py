from django.shortcuts import render, redirect
from cadmin import forms
# Create your views here.


def login(request):
    pass


def logout(request):
    pass


def register(request):
    if request.method == "POST":
        f = forms.RegisterForm(request.POST)
        if f.is_valid():
            f.save()

            redirect('dashboard')
    f = forms.RegisterForm()
    return render(request, 'cadmin/register.html', {"form": f})
