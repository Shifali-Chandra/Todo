"""NO NEED FOR THIS"""
from dataclasses import field, fields
from django import forms
from todo.models import Todo
from django.utils import timezone

class TodoForm(forms.Form):
    title = forms.CharField(required=True)
    description = forms.CharField(required=True)
    created_date = forms.DateTimeField(required=False)
    due_date = forms.DateTimeField(required=False)

class TaskForm(forms.ModelForm):
    title = forms.CharField(required=True)
    description = forms.CharField(required=True)
    created_date = forms.DateTimeField(required=False)
    due_date = forms.DateTimeField(required=False)

    class Meta:
        model = Todo
        fields ='__all__'
        exclude = ['completed']
        

    