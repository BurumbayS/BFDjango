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

class Post(models.Model) :
    title = models.CharField(max_length = 50)
    content = models.TextField()
    date = models.DateField(auto_now = True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    @classmethod
    def create(cls, title, content, username):
        user = User.objects.filter(username = username)
        post = cls(title = title, content = content, author = user[0])

        return post

class Comment(models.Model) :
    content = models.TextField()
    date = models.DateField(auto_now = True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    @classmethod
    def create(cls, content, username, post_id):
        user = User.objects.filter(username = username)
        post = Post.objects.filter(id = post_id)
        comment = cls(content = content, author = user[0], post = post[0])

        return comment
