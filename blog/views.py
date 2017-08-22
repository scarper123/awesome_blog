from django.shortcuts import render, get_list_or_404
from blog import models as blog_models
from awesome_blog import helpers


# Create your views here.


def post(request):
    post_list = blog_models.Post.objects.all()
    posts = helpers.pg_records(request, post_list)
    return render(request, 'blog/post_list.html', {"posts": posts})


def hello_world(request):
    return render(request, 'blog/base.html')
