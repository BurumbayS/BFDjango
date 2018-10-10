from django.db import models

# Create your models here.

class User(models.Model) :
    username = models.CharField(max_length = 20, unique = True)
    password = models.CharField(max_length = 20)
    first_name = models.CharField(max_length = 30, blank=True)
    last_name = models.CharField(max_length = 30, blank=True)

    @classmethod
    def create(cls, username, password, first_name, last_name):
        user = cls(username = username, password = password, first_name = first_name, last_name = last_name)

        return user

class Task(models.Model) :
    title = models.CharField(max_length = 50)
    created_date = models.DateField(auto_now = True)
    due_on = models.DateField()
    owner = models.ForeignKey(User, on_delete = models.CASCADE)
    is_done = models.BooleanField(default = False)

    @classmethod
    def create(cls, title, due_on, username):
        user = User.objects.filter(username = username)
        task = cls(title = title, due_on = due_on, owner = user[0])

        return task
