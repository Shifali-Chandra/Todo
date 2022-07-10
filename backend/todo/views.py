from django.http import HttpResponse
from django.shortcuts import render, redirect,get_object_or_404
from rest_framework import viewsets
from .serializers import TodoSerializers
from .models import Todo, UserProfile
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from todo.forms import TodoForm, TaskForm
from todo.views import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
# Create your views here.

# class clientLoginView(LoginView):
# 	template_name = "registrations/login.html"
# 	redirect_authenticated_user = True
# 	def get_success_url(self):
# 		return reverse_lazy(viewTodoView)


class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializers
    queryset = Todo.objects.all()

# def index(request):
# 	if request.user.is_authenticated() == False:
# 		return render(request, 'registration/login.html')
# 	return redirect('/viewTodoItem/')

@login_required
def viewTodoView(request):
	# user = get_object_or_404(User, username=User.username)
	#tasks = Todo.objects.filter(user_id=request.user).values()
	# task = Todo.objects.get(user=request.user)
	tasks = Todo.objects.filter(user=request.user).values()
	print(tasks)
	context = {'Tasks': tasks}
	return render(request, 'todo/viewTodoItem.html', context)

def addtask(request):
	if request.method =="POST":
		f_title = request.POST['title'] 
		f_description = request.POST['description'] 
		f_created_date =request.POST['SD']
		f_due_date = request.POST['CD']
		print(request.POST)
		Todo.objects.create(user = request.user, title=f_title, description = f_description, completed = False, created_date=f_created_date, due_date=f_due_date)
		return redirect('/viewTodoItem/')	

def removetask(request, p_title):
	item = Todo.objects.get(title=p_title)
	item.delete()
	return redirect('/viewTodoItem/')


def removeAll(request):
	items_list = Todo.objects.filter(user=request.user)
	items_list.delete()
	return redirect('/viewTodoItem/')

def updateTask(request):
	todo = Todo.objects.get(request)
	if request.method =="POST":
		f_title = request.POST['title'] 
		f_description = request.POST['description'] 
		f_created_date =request.POST['SD']
		f_due_date = request.POST['CD']
		print(request.POST)
		Todo.objects.create(title=f_title, description = f_description, completed = False, created_date=f_created_date, due_date=f_due_date)
		return redirect('/viewTodoItem/')
	todo.complete = True
	todo.save()
	return redirect('index')

def details(request):
	tasks = Todo.objects.filter(user=request.user)
	context = {'Tasks': tasks}
	return render(request, 'todo/detailsTodoItem.html', context)





def add(request):
	if request.method =="POST":
		form = TaskForm(request.POST)
		print(request.POST)
		if form.is_valid():
			f_title = request.POST.get('title') 
			f_description = request.POST.get('description') 
			f_created_date =request.POST.get('created_date')
			f_due_date = request.POST.get('due_date') 
			todoObj = Todo(title=f_title, description = f_description, completed = False, created_date = f_created_date, due_date= f_due_date)
			form.save()
		# tasks = Todo.objects.all()
		# context = {'Tasks': tasks}
		return redirect('/viewTodoItem/')
	return render(request, 'todo/viewTodoItem.html', {'form': TaskForm})

def addTodoView(request):
	task = TaskForm()
	return render(request, 'todo/addTodoItem.html', {"form": task})

def completeTodo(request, todo_id):
	todo = Todo.objects.get(pk=todo_id)
	todo.complete = True
	todo.save()
	return redirect('index')


