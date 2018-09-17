from django.db import models

# Create your models here.
class Task(models.Model) :
    title = models.CharField(max_length = 50)
    created_date = models.DateField()
    due_on = models.DateField()
    owner = models.CharField(max_length = 50, default = 'admin')
    is_done = models.BooleanField(default = False)
