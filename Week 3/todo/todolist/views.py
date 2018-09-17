from django.shortcuts import render
from django.http import HttpResponse
from todolist.models import Task

# Create your views here.
def todolist(request):
    tasks = Task.objects.filter(is_done = False)
    context = {
        'tasks' : tasks
    }
    return render(request, 'todolist.html', context)

def deleteTodolist(request):
    tasks = Task.objects.filter(is_done = False).delete()
    return render(request, 'todolist.html')

def completedList(request) :
    tasks = Task.objects.filter(is_done = True)
    context = {
        'tasks' : tasks
    }
    return render(request, 'completedlist.html', context)

def deleteCompletedList(request) :
    tasks = Task.objects.filter(is_done = True).delete()
    return render(request, 'completedlist.html', context)
