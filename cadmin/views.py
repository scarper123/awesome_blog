from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import login_required
from cadmin import forms


# Create your views here.

# https://docs.djangoproject.com/en/1.11/topics/auth/default/
def login(request, **kwargs):
    if request.method == "POST":
        if request.user.is_authenticated():
            return redirect('dashboard')
    return auth_views.LoginView.as_view(**kwargs)(request, **kwargs)


@login_required
def logout(request, **kwargs):
    return auth_views.LogoutView.as_view(**kwargs)(request, **kwargs)


def register(request):
    if request.method == "POST":
        f = forms.RegisterForm(request.POST)
        if f.is_valid():
            f.save()

            return redirect('dashboard')
    else:
        f = forms.RegisterForm()
    return render(request, 'cadmin/register.html', {"form": f})


@login_required
def profile(request):
    return render(request, 'cadmin/profile.html')
