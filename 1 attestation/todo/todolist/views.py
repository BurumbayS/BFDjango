from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from todolist.models import Task, User
from django.contrib.auth import authenticate

# Create your views here.
def logout(request) :
    request.session['authorized'] = False

    return todolist(request)

def login(request) :
    username = request.POST.get("username", " ")
    password = request.POST.get("password", " ")
    user = User.objects.filter(username = username, password = password)

    if user.count() > 0 is not None:
        request.session['username'] = user[0].username
        request.session['authorized'] = True
    else:
        request.session['authorized'] = False

    return todolist(request)

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

    return todolist(request)



def addNewTask(request) :
    task_title = request.POST.get("task_title"," ")
    task_due_on = request.POST.get("task_due_on"," ")
    task = Task.create(task_title, task_due_on, request.session['username'])
    task.save()
    return todolist(request)

def todolist(request):
    if request.session.get('authorized', False) :
        user = User.objects.filter(username = request.session['username'])
        tasks = Task.objects.filter(is_done = False, owner = user[0])
        context = {
            'authorized' : True,
            'user' : user[0].first_name + ' ' +  user[0].last_name,
            'tasks' : tasks
        }
    else :
        tasks = Task.objects.filter(is_done = False)
        context = {
            'authorized' : False,
            'tasks' : tasks
        }

    return render(request, 'todolist.html', context)

def deleteTodolist(request):
    tasks = Task.objects.filter(is_done = False).delete()
    return render(request, 'todolist.html')

def addToTodolist(request) :
    task_id = request.POST.get("task_id"," ")
    Task.objects.filter(id = task_id).update(is_done = False);
    tasks = Task.objects.filter(is_done = True)
    context = {
        'tasks' : tasks
    }
    return render(request, 'completedlist.html', context)

def completedList(request) :
    tasks = Task.objects.filter(is_done = True)
    context = {
        'tasks' : tasks
    }
    return render(request, 'completedlist.html', context)

def deleteCompletedList(request) :
    tasks = Task.objects.filter(is_done = True).delete()
    return render(request, 'completedlist.html')

def addToCompletedList(request) :
    task_id = request.POST.get("task_id"," ")
    Task.objects.filter(id = task_id).update(is_done = True);
    tasks = Task.objects.filter(is_done = False)
    context = {
        'tasks' : tasks
    }
    return render(request, 'todolist.html', context)
