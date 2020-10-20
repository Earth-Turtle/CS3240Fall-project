from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from django.views.generic import TemplateView
from home import views



urlpatterns = [
    #ex: '/'
    path('', views.IndexView.as_view(), name='home'),

    #ex: '/admin/'
    path('admin/', admin.site.urls, name='admin'),

    #ex: '/accounts/'
    path('accounts/', include('allauth.urls'), name='accounts'),

    path('categories/', views.categories, name='categories'),

    path('categories/<slug:categorySlug>/', views.singleCategory, name='singleCategory'),
    path('categories/<slug:categorySlug>/<slug:postSlug>/', views.comment, name='comment'),
    path('post-comment/', views.postComment, name='postComment'),

    path('logout/', views.logout, name='logout'),
]
