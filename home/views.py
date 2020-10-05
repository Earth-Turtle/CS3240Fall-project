from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

# Create your views here.


class IndexView(generic.TemplateView):
    template_name = 'home/index.html'

def accounts_view(request):
    return render(request, "accounts.html")
