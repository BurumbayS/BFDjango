# Generated by Django 2.0.8 on 2018-09-15 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_on',
            field=models.DateField(),
        ),
    ]
