from django.contrib.auth import models as auth_models
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http.response import JsonResponse
from awesome_blog import helpers
from blog import forms as blog_forms
from blog import models as blog_models


# Create your views here.


def post_list(request, json=False):
    posts = blog_models.Post.objects.all()
    posts = helpers.pg_records(request, posts)
    if json:
        data = [post.json() for post in posts]
        return JsonResponse(data, safe=False)
    return render(request, 'blog/post_list.html', {"posts": posts})


def post_detail(request, pid):
    p = get_object_or_404(blog_models.Post, id=pid)
    return render(request, 'blog/post_detail.html', {"post": p})


@login_required
def post_add(request):
    if request.method == "POST":
        f = blog_forms.PostForm(request.POST)
        if f.is_valid():
            model_save(request, f, blog_models.Author)
            return redirect('post_list')
    else:
        f = blog_forms.PostForm()

    return render(request, 'blog/post_add.html', {"form": f})


def post_delete(request, pid):
    return None


def post_update(request, pid):
    return None


def category_list(request):
    return None


def category_detail(request):
    return None


@login_required
def category_add(request):
    if request.method == "POST":
        f = blog_forms.CategoryForm(request.POST)
        if f.is_valid():
            model_save(request, f, blog_models.Author)
            messages.add_message(request, messages.INFO, "Add category %s succeed." % f.cleaned_data['name'])
            return redirect('dashboard')
    else:
        f = blog_forms.CategoryForm()

    return render(request, 'blog/category_add.html', {"form": f})


def category_delete(request):
    return None


def category_update(request):
    return None


@login_required
def tag_add(request):
    if request.method == "POST":
        f = blog_forms.TagForm(request.POST)
        if f.is_valid():
            model_save(request, f, blog_models.Author)
            messages.add_message(request, messages.INFO, "Add tag %s succeed." % f.cleaned_data['name'])
            return redirect('dashboard')
    else:
        f = blog_forms.TagForm()

    return render(request, 'blog/tag_add.html', {"form": f})


def model_save(request, form, author_model, **kwargs):
    """
    Save model.
    1. request.user is superuser and no choice author, save with default user is staff
    2. request.user is superuser and no choice author, save directly
    3. request.user is not superuser, save with login user
    
    Example:
        >>> model_save(request, blog_forms.TagForm(request.POST), blog_models.Post)
    """
    params = {}
    params.update(kwargs)

    def save_with_user():
        author = get_object_or_404(author_model, **params)
        tag = form.save(commit=False)
        tag.author = author
        tag.save()
        form.save_m2m()

    if request.POST.get("author") == "" and request.user.is_superuser:
        params["user__username"] = "staff"
        save_with_user()
    elif request.POST.get("author") and request.user.is_superuser:
        form.save()
    else:
        params["user__username"] = request.user.username
        save_with_user()
