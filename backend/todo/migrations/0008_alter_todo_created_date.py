# Generated by Django 3.2.13 on 2022-07-09 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0007_todo_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]