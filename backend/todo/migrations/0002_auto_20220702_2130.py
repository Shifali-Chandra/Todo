# Generated by Django 3.2.13 on 2022-07-02 16:00

from django.db import migrations, models
import django.utils.timezone
import todo.models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='todo',
            name='due_date',
            field=models.DateTimeField(default=todo.models.one_week_hence),
        ),
    ]