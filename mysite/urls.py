from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from django.views.generic import TemplateView
from home import views



urlpatterns = [
    path('', TemplateView.as_view(template_name='home/index.html')),
    path('accounts/', views.accounts_view, name='accounts'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    
]
