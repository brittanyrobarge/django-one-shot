from django.shortcuts import render, get_object_or_404
from .models import TodoList

# Create your views here.
def todo_list_view(request):
    todo_lists = TodoList.objects.all()
    context = {'todo_lists': todo_lists}
    return render(request, 'todos/todo_list.html', context)

def todo_list_detail(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    todo_items = todo_list.items.all() 
    context = {'todo_list': todo_list, 'todo_items': todo_items}
    return render(request, 'todos/todo_list_detail.html', context)
