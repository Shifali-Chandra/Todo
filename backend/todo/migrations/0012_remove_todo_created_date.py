# Generated by Django 3.2.13 on 2022-07-10 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0011_alter_todo_created_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='created_date',
        ),
    ]
