from django.urls import path, re_path
from todolist import views

urlpatterns = [
    path('', views.todolist),
    path('delete/', views.deleteTodolist),
    path('completedList/', views.completedList),
    path('completedList/delete/', views.deleteCompletedList),
]
