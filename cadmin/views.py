from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http.response import JsonResponse

from cadmin import forms


# Create your views here.

# https://docs.djangoproject.com/en/1.11/topics/auth/default/
def login(request, **kwargs):
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
def profile(request, json=False):
    if json:
        user = request.user
        data = {'username': user.username,
                'email': user.email,
                'active': user.is_active,
                'staff': user.is_staff,
                'superuser': user.is_superuser,
                'date_join': user.date_joined,
                'last_login': user.last_login
                }
        return JsonResponse(data, safe=False)
    return render(request, 'cadmin/profile.html')
