from django.db import models
from django.contrib.auth.models import User


# Create your models here.
#


class Author(models.Model):
    user = models.OneToOneField(User)
    phone = models.IntegerField(default=12345678911)
    activation_key = models.CharField(default=1, max_length=255)
    email_validated = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def __str__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(Author)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categorys"

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    category = models.ForeignKey(Category)
    author = models.ForeignKey(Author)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title
