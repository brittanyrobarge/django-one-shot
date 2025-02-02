from django.shortcuts import render, get_object_or_404, redirect
from .models import TodoList,TodoItem
from .forms import TodoListForm, TodoItemForm

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

def todo_list_create(request):
    if request.method == 'POST':
        form = TodoListForm(request.POST)
        if form.is_valid():
            todo_list = form.save()
            return redirect('todo_list_detail', id=todo_list.id)
    else:
        form = TodoListForm()
    return render(request, 'todos/todo_list_create.html', {'form':form})

def todo_list_update(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    if request.method == 'POST':
        form = TodoListForm(request.POST, instance=todo_list)
        if form.is_valid():
            form.save()
            return redirect('todo_list_detail', id=id)
    else:
        form = TodoListForm(instance=todo_list)
    return render(request, 'todos/todo_list_update.html', {'form': form})

def todo_list_delete(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    if request.method == 'POST':
        todo_list.delete()
        return redirect('todo_list_list')
    return render(request, 'todos/todo_list_delete.html')

def todo_item_create(request):
    if request.method == 'POST':
        form = TodoItemForm(request.POST)
        if form.is_valid():
            todo_item = form.save(commit=False)
            todo_item.list = TodoList.objects.first()
            todo_item.save()
            return redirect('todo_list_detail', id=todo_item.list.id)
    else:
        form = TodoItemForm()
    return render(request, 'todos/todo_item_create.html', {'form': form})

def todo_item_update(request, id):
    todo_item = get_object_or_404(TodoItem, id=id)
    if request.method == 'POST':
        form = TodoItemForm(request.POST, instance=todo_item)
        if form.is_valid():
            form.save()
            return redirect('todo_list_detail', id=todo_item.list.id)
    else:
        form = TodoItemForm(instance=todo_item)
    return render(request, 'todos/todo_item_update.html', {'form': form})
