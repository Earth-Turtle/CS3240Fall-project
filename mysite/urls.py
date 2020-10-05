from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from home import views



urlpatterns = [
    path('', views.home_view, name='home'),
    path('accounts/', views.accounts_view, name='accounts')

    
]
