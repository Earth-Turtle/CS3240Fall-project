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

    # IF USER HAS USER PROFILE MADE, pull from that data
    try:
        profile = UserProfile.objects.get(user=request.user)
        data['email'] = profile.my_email
        data['first_name'] = profile.my_first_name
        data['last_name'] = profile.my_last_name
        data['phone'] = profile.phone

    # If user does not have user profile made, pull from the standard user data

    except:  # change to extend exception?
        data['email'] = request.user.email
        data['first_name'] = request.user.first_name
        data['last_name'] = request.user.last_name
    return render(request, "my-profile.html", data)


def myProfileAction(request):

    # Take in the data from the button press
    dataIn = request.POST.copy()

    # If the profile has been made, get the objects from the profile
    try:
        new_profile = UserProfile.objects.get(user=request.user)

    # If the profile has not been made, create a new profile that extends the default user
    # profile from the authentication
    except:
        new_profile = UserProfile() # Create new user profile
        new_profile.user = User.objects.get(id=request.user.id) # Populate user field with extension from default user

    # NOTE: the following will only save phone number, not the other stuff; will figure out how to do that later
    new_profile.my_first_name = dataIn['first_name']  # Save inputted first name in the my_first_name field
    new_profile.my_last_name = dataIn['last_name']  # Save inputted last name in the my_last_name field
    new_profile.my_email = dataIn['email']  # Save inputted email in the my_email field
    new_profile.phone = dataIn['phone']  # Save inputted phone number in the phone field
    new_profile.save()  # Save changes made to the UserProfile
    ###update here

    return redirect('/')
