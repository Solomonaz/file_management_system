from django.shortcuts import render, redirect
from .forms import Formtask
from .models import ModelTask
from django.urls import reverse
from django.contrib import messages
from django.db.models import Q


def index(request):
    username=None
    form = Formtask()
    todo_list = ModelTask.objects.order_by('-created_at')
    if request.method == 'POST':
        # print(todo_list)
        form = Formtask(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'username':username,
        'todo_list':todo_list,
        'form':form
    }
    messages.success(request, 'Task successfully added.')
    return render(request, 'index.html', context)

def delete(request, id):
    todo_delete = ModelTask.objects.get(id=id)
    todo_delete.delete()
    messages.success(request, 'You have Deleted a task')
    return redirect(reverse('index'))

def edit(request, id):
    todo_edit_model = ModelTask.objects.get(pk=id)
    todo_edit_form = Formtask(request.POST or None, instance=todo_edit_model)
    if todo_edit_form.is_valid():
        todo_edit_form.save()
        messages.success(request, ' You have updated a task.')
        return redirect('index')
        
    context = {
        # 'todo_edit_model':todo_edit_model,
        'todo_edit_form':todo_edit_form
    }
    return render(request, 'edit.html', context)
    # return redirect(reverse('index'))

def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            result = ModelTask.objects.order_by('created_at').filter(Q(task_name__icontains=keyword))
            task_count = result.count()
    context = {
        'result':result,
        'task_count':task_count
    }

    return render(request, 'index.html', context)