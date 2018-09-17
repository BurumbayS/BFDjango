# Generated by Django 2.0.8 on 2018-09-15 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('created_date', models.DateTimeField()),
                ('due_on', models.DateTimeField()),
                ('owner', models.CharField(default='admin', max_length=50)),
                ('is_done', models.BooleanField(default=False)),
            ],
        ),
    ]
