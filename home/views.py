from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic

from django.conf import settings
from .models import Category
from .models import Post
from .models import Comment
#from django.contrib.auth import authenticate
#from django.contrib.auth.models import Permission
#from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import logout
# Create your views here.


class IndexView(generic.TemplateView):
    template_name = 'home/index.html'

def accounts_view(request):
        return render(request, "accounts.html")


def categories(request):
    catgories = list(Category.objects.all())

    return render(request,"categories.html",{'catgories':catgories})


def singleCategory(request, categorySlug):
    getCategory = Category.objects.get(slug=categorySlug)
    posts = list(Post.objects.filter(category=getCategory))


    return render(request,"posts.html",{'posts':posts})


def singleCategory(request, categorySlug):
    getCategory = Category.objects.get(slug=categorySlug)
    posts = list(Post.objects.filter(category=getCategory))


    return render(request,"posts.html",{'posts':posts})


def comment(request, categorySlug, postSlug):
    getCategory = Category.objects.get(slug=categorySlug)
    post = Post.objects.get(slug=postSlug)
    comments = list(Comment.objects.filter(post=post))

    return render(request,"comment.html",{'post':post, 'comments':comments})


def postComment(request):
    dataIn = request.POST.copy()
    post = dataIn['post']
    name = dataIn['name']
    comments = dataIn['comments']


    commentModel = Comment()
    commentModel.post = Post.objects.get(id=post)
    commentModel.author = name
    commentModel.text = comments
    commentModel.save()

    return redirect('/categories/')


def logout(request):
    logout(request)