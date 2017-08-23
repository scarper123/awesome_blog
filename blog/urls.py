"""awesome_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from blog import views

urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^post/$', views.post_list, name='post_list'),
    url(r'^post/api/$', views.post_list, kwargs={'json': True}, name='post_list'),
    url(r'^post/<?P([\d]+)>/$', views.post_detail, name='post_detail'),
    url(r'^post/add/$', views.post_add, name='post_add'),
    url(r'^post/delete/<?P([\d]+)>/$', views.post_delete, name='post_delete'),
    url(r'^post/update/<?P([\d]+)>/$', views.post_update, name='post_update'),

    url(r'^category/$', views.category_list, name='category_list'),
    url(r'^category/<?P([\d]+)>/$', views.category_detail, name='category_detail'),
    url(r'^category/add/$', views.category_add, name='category_add'),
    url(r'^category/delete/<?P([\d]+)>/$', views.category_delete, name='category_delete'),
    url(r'^category/update/<?P([\d]+)>/$', views.category_update, name='category_update'),

    url(r'^tag/$', views.category_list, name='category_list'),
    url(r'^tag/<?P([\d]+)>/$', views.category_detail, name='category_detail'),
    url(r'^tag/add/$', views.tag_add, name='tag_add'),
    url(r'^tag/delete/<?P([\d]+)>/$', views.category_delete, name='category_delete'),
    url(r'^tag/update/<?P([\d]+)>/$', views.category_update, name='category_update'),
]
