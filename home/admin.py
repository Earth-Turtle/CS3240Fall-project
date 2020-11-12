from django.contrib import admin
from .models import Category
from .models import Post
from .models import Comment, UserProfile
from .models import Suggestions

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(UserProfile)
admin.site.register(Suggestions)
# Register your models here.
