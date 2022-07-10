# Generated by Django 3.2.13 on 2022-07-10 07:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0012_remove_todo_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]