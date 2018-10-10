from django.contrib import admin
from todolist.models import Task
from todolist.models import User

# Register your models here.
admin.site.register(Task)
admin.site.register(User)
