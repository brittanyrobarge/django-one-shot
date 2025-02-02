from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list_view, name='todo_list_list'),
    path('<int:id>/', views.todo_list_detail, name='todo_list_detail'),
    path('create/', views.todo_list_create, name='todo_list_create'),
    path('<int:id>/edit/', views.todo_list_update, name='todo_list_update'),
    path('<int:id>/delete/', views.todo_list_delete, name='todo_list_delete'),
    path('items/create/', views.todo_item_create, name='todo_item_create'),
    path('items/<int:id>/edit/', views.todo_item_update, name='todo_item_update'),
]
