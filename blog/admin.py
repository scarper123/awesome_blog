from django.contrib import admin

from blog import models


# Register your models here.
# https://docs.djangoproject.com/en/1.11/ref/contrib/admin/
@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user',)


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'author')


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'author')


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
