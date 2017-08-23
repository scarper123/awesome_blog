# -*- coding: UTF-8 -*-
from django import forms

from blog import models

__authors__ = "Shanming Liu"


class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ('title', 'content', 'category', 'tags', 'author')


class CategoryForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = ('name', 'slug', 'author')


class TagForm(forms.ModelForm):
    class Meta:
        model = models.Tag
        fields = ('name', 'slug', 'author')


class AuthorForm(forms.ModelForm):
    class Meta:
        model = models.Author
        fields = ('user', 'phone')
