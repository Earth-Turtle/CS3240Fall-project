from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(null=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    publish = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    my_first_name = models.CharField(max_length=100, default="")
    my_last_name = models.CharField(max_length=100, default="")
    my_email = models.CharField(max_length=100, default="")
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.my_email


class Suggestions(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.TextField()
    message = models.TextField(default="")

    def __str__(self):
        return self.name
