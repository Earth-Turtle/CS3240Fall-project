from django.db import models
from django.utils import timezone
from django.contrib.auth.models import Permission, User
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404

# Create your models here.

<<<<<<< HEAD
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10, default="55555555555")

    def __str__(self):
        return self.first_name + ' ' + self.last_name

=======
>>>>>>> 7f74d0abf14ad28569ec3f7ba987ddc2281ff347
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
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text


    