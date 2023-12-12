from django.contrib import admin
from .models import TodoList, TodoItem

# Register your models here.
@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(TodoItem)
class TodoItemAdmin(admin.ModelAdmin):
    list_display = ('task', 'due_date', 'is_completed')
