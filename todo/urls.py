from django.urls import path 
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.Login.as_view(),name='login'),
    path('todo_create_list/',views.TodoListView.as_view(),name='list_todo_create'),
    path('todo_update_delete/<int:pk>/',views.RetrieveTodoView.as_view(),name='todo_retrive_view'),
]
