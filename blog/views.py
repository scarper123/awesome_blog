from django.shortcuts import render, get_list_or_404
from blog import models as blog_models
# Create your views here.


def post_list(request):
    posts = get_list_or_404(blog_models.Post)
    return render(request, 'blog/post_list.html', {"posts": posts})


def hello_world(request):
    return render(request, 'blog/base.html')
