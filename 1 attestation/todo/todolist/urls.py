from django.urls import path, re_path
from todolist import views

urlpatterns = [
    path('', views.todolist),
    path('auth/login/', views.login),
    path('auth/signup/', views.signup),
    path('auth/logout/', views.logout),
    path('addTask/', views.addNewTask),
    path('delete/', views.deleteTodolist),
    path('add/', views.addToTodolist),
    path('completedList/', views.completedList),
    path('completedList/delete/', views.deleteCompletedList),
    path('completedList/add/', views.addToCompletedList),
]
