from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list_view, name='todo_list_list'),
    path('<int:id>/', views.todo_list_detail, name='todo_list_detail'),
    path('create/', views.todo_list_create, name='todo_list_create'),
    path('<int:id>/edit/', views.todo_list_update, name='todo_list_update'),
]
