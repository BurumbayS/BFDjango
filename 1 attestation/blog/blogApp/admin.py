from django.contrib import admin
from blogApp.models import Post, User, Comment

# Register your models here.
admin.site.register(Post)
admin.site.register(User)
admin.site.register(Comment)
