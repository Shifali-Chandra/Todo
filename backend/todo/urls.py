from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.viewTodoView),
    #path('', views.index),
    # path('login/', views.clientLoginView, name='login'),
        #path('tasks/', views.add, name='add'),
    #path('addTodoItem/', views.addTodoView),
    path('addtask/', views.addtask, name='addtask'),
    path('detailsTodoItem/', views.details, name='details'),
    path('removetask/<str:p_title>/', views.removetask, name='removetask'),
    path('removeAll/', views.removeAll, name='removeAll'),
    path('viewTodoItem/', views.viewTodoView, name='home'), 
]