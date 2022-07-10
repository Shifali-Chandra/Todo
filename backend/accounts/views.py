from django.shortcuts import render, redirect
from todo.views import viewTodoView
# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import auth
from todo.views import viewTodoView


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy(viewTodoView)
    template_name = "registration/signup.html"

def logout(request):
    auth.logout(request)
    return render(request, 'todo/viewTodoItem.html')
