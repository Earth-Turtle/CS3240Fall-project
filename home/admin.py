from django.contrib import admin
from .models import Category
from .models import Post
from .models import Comment, UserProfile

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(UserProfile)
# Register your models here.
