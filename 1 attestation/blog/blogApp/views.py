from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from blogApp.models import Post, User, Comment

# Create your views here.
def logout(request) :
    request.session['authorized'] = False

    return blog(request)

def login(request) :
    username = request.POST.get("username", " ")
    password = request.POST.get("password", " ")
    user = User.objects.filter(username = username, password = password)

    if user.count() > 0 is not None:
        request.session['username'] = user[0].username
        request.session['authorized'] = True
    else:
        request.session['authorized'] = False

    return blog(request)

def signup(request) :
    first_name = request.POST.get("first_name", " ")
    last_name = request.POST.get("last_name", " ")
    username = request.POST.get("username", " ")
    password = request.POST.get("password", " ")
    confirm_password = request.POST.get("confirm_password", " ")

    if password == confirm_password :
        user = User.create(username, password, first_name, last_name)
        user.save()
        request.session['username'] = username
        request.session['authorized'] = True
    else:
        request.session['authorized'] = False

    return blog(request)


def blog (request) :
    if request.session.get('authorized', False) :
        user = User.objects.filter(username = request.session['username'])
        context = {
            'authorized' : True,
            'user' : user[0],
        }
    else :
        context = {
            'authorized' : False,
        }

    queryset = Post.objects.all()
    posts = reversed(list(queryset))
    posts_w_comments = list()
    for post in posts :
        comments = Comment.objects.filter(post = post)
        posts_w_comments.append({ 'post' : post, 'comments' : comments })

    context['posts'] = posts_w_comments

    return render(request, 'blog.html', context)

def addComment(request) :
    post_id = request.POST.get("post_id", " ")
    print (post_id)
    content = request.POST.get("comment", " ")
    if request.session.get('authorized', False) :
        username = request.session['username']
    else :
        username = 'anonymous'

    comment = Comment.create(content, username, post_id)
    comment.save()

    return blog(request)

def addPost(request) :
    title = request.POST.get("title", " ")
    content = request.POST.get("content", " ")
    post = Post.create(title, content, request.session['username'])
    post.save()

    return blog(request)
