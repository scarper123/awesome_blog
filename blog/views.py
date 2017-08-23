from django.contrib.auth import models as auth_models
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from awesome_blog import helpers
from blog import forms as blog_forms
from blog import models as blog_models


# Create your views here.


def post_list(request):
    posts = blog_models.Post.objects.all()
    posts = helpers.pg_records(request, posts)
    return render(request, 'blog/post_list.html', {"posts": posts})


def post_detail(request, pid):
    p = get_object_or_404(blog_models.Post, id=pid)
    return render(request, 'blog/post_detail.html', {"post": p})


@login_required
def post_add(request):
    if request.method == "POST":
        f = blog_forms.PostForm(request.POST)
        if f.is_valid():
            model_save(request, f, blog_models.Post)
            redirect('post_list')
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
            model_save(request, f, blog_models.Category)
            redirect('category_list')
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
            return redirect('category_list')
    else:
        f = blog_forms.TagForm()

    return render(request, 'blog/tag_add.html', {"form": f})


def model_save(request, form, model, **kwargs):
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
        author = get_object_or_404(model, **params)
        tag = form.save(commit=False)
        tag.author = author
        tag.save()
        form.save_m2m()

    if request.POST.get("author") == "" and request.user.is_superuser:
        params["author__user__username"] = "staff"
        save_with_user()
    elif request.POST.get("author") and request.user.is_superuser:
        form.save()
    else:
        params["author__user__username"] = request.user.username
        save_with_user()


@login_required
def author_add(request):
    if request.method == "POST":
        f = blog_forms.AuthorForm(request.POST)
        if f.is_valid():
            if request.POST.get("author") == "" and request.user.is_superuser:
                user = get_object_or_404(auth_models.User, user__username='staff')
                author = f.save(commit=False)
                author.user = user
                author.save()
                f.save_m2m()
            elif request.POST.get("author") and request.user.is_superuser:
                f.save()
            else:
                user = get_object_or_404(auth_models.User, user__username=request.user.username)
                author = f.save(commit=False)
                author.user = user
                author.save()
                f.save_m2m()
            return redirect('author_list')
    else:
        f = blog_forms.AuthorForm()

    return render(request, 'blog/author_add.html', {"form": f})
