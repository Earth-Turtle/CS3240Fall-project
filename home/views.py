from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views import generic


from .models import Category
from .models import Post
from .models import Comment, UserProfile
from django.contrib.auth.models import User


# Create your views here.


class IndexView(generic.TemplateView):
    template_name = 'home/index.html'

def accounts_view(request):
    return render(request, "accounts.html")


def categories(request):
    catgories = list(Category.objects.all())
    return render(request,"categories.html",{'catgories':catgories})


def singleCategory(request, categorySlug):
    get_category = Category.objects.get(slug=categorySlug)
    posts = list(Post.objects.filter(category=get_category))
    
    return render(request,"posts.html",{'posts':posts, 'category':get_category})


def comment(request, categorySlug, postSlug):
    get_category = Category.objects.get(slug=categorySlug)
    post = Post.objects.get(slug=postSlug)
    comments = list(Comment.objects.filter(post=post))

    return render(request,"comment.html",{'post':post, 'comments':comments, 'category':get_category})


def postComment(request):
    dataIn = request.POST.copy()
    post = dataIn['post']
    name = dataIn['name']
    comments = dataIn['comments']

    comment_model = Comment()
    comment_model.post = Post.objects.get(id=post)
    comment_model.author = name
    comment_model.text = comments
    comment_model.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    
def myProfile(request):
    data = {}
    try:
        profile = UserProfile.objects.get(user=request.user)
        data['email'] = profile.user.email
        data['first_name'] = profile.user.first_name
        data['last_name'] = profile.user.last_name
        data['phone'] = profile.phone

    except: #NOT SECURE: FIND BETTER WAY TO DO THIS
        data['email'] = request.user.email
        data['first_name'] = request.user.first_name
        data['last_name'] = request.user.last_name
    return render(request,"my-profile.html",data)


def myProfileAction(request):
    dataIn = request.POST.copy()

    try:
        new_profile = UserProfile.objects.get(user=request.user)
    except:
        new_profile = UserProfile()
        new_profile.user = User.objects.get(id=request.user.id)

    #NOTE: the following will only save phone number, not the other stuff; will figure out how to do that later
    new_profile.user.first_name = dataIn['first_name']
    new_profile.user.last_name = dataIn['last_name']
    new_profile.user.email = dataIn['email']
    new_profile.phone = dataIn['phone']
    new_profile.save()
    ###update here

    return redirect('/')
