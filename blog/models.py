from django.contrib.auth.models import User
from django.db import models


# Create your models here.
#


class Author(models.Model):
    user = models.OneToOneField(User)
    phone = models.IntegerField(default=1, blank=True)
    activation_key = models.CharField(default=1, max_length=255)
    email_validated = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def json(self):
        return {'username': self.user.username,
                'email': self.user.email,
                'phone': self.phone,
                'active': self.user.is_active,
                'staff': self.user.is_staff,
                'superuser': self.user.is_superuser,
                'date_join': self.user.date_joined,
                'last_login': self.user.last_login
                }

    def __str__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(Author, blank=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def json(self):
        return {
            "name": self.name,
            "slug": self.slug,
            "author": self.author.json()
        }

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(Author, blank=True)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def json(self):
        return {
            "name": self.name,
            "slug": self.slug,
            "author": self.author.json()
        }

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(Author, blank=True)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def json(self):
        return {
            "title": self.title,
            "content": self.content,
            "pub_date": self.pub_date,
            "category": self.category.json(),
            "tags": [tag.json() for tag in self.tags.all()],
            "author": self.author.json()
        }

    def __str__(self):
        return self.title
