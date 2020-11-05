from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views import generic
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError

from .models import Category
from .models import Post
from .models import Comment


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
    data['email'] = request.user.email
    data['first_name'] = request.user.first_name
    data['last_name'] = request.user.last_name

    return render(request,"my-profile.html",data)


def myProfileAction(request):
    dataIn = request.POST.copy()
    userModel = User.objects.get(id=request.user.id)
    userModel.first_name = dataIn['first_name']
    userModel.last_name = dataIn['last_name']
    userModel.email = dataIn['email']
    # userModel.phone = dataIn['phone']
    userModel.save()
    ###update here

    return redirect('/')

def contact_form(request):
    form = ContactForm()
    text = request.GET.get('text', '')

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = f'Message from {form.cleaned_data["name"]}'

            dataIn = request.POST.copy()
            message = dataIn["message"]
            sender = dataIn["email"]
            recipient_email = dataIn["recipient_email"]
            recipients = [recipient_email]

            # print(subject)
            # print(message)
            # print(sender)
            # print(recipient_email)
            try:
                send_mail(subject, message, sender, recipients, fail_silently=True)
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return HttpResponse('Success...Your email has been sent')
    return render(request,"contact.html",{'form':form, 'text': text})


# Contact From/ Sendgrid template taken from: https://github.com/the-kodechamp/django_blog_tutorial/blob/master/blog/templates