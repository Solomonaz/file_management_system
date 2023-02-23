from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotFound
import os
from django.urls import reverse
from .models import Project_List
from .forms import ProjectListForm



def index(request):
    return render(request, 'index.html')

def report(request):
    return render(request, 'pages/report.html')

def project_list(request):
    project_list = Project_List.objects.all()
    context = {
        'project_list':project_list
    }
    return render(request, 'pages/project_list.html',context)

def del_project(request,id):
    del_project = Project_List.objects.get(id=id)
    del_project.delete()
    return redirect(reverse('project_list'))

def edit_project(request, id):
    project = get_object_or_404(Project_List, id=id)
    if request.method == 'POST':
        form = ProjectListForm(request.post, instance=project)
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
            return redirect('project_list', pk=project.pk)
    else:
        form = ProjectListForm(instance=project)
        context = {
            'form': form
            }
    return render(request, 'pages/project_list.html', context)


def new_project(request):
    # username=None
    form = ProjectListForm()
    project_list = Project_List.objects.order_by('-date_created')
    if request.method == 'POST':
        # print(todo_list)
        form = ProjectListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('new_project')
    context = {
        # 'username':username,
        'project_list':project_list,
        'form':form
    }
    # messages.success(request, 'Task successfully added.')
    return render(request, 'pages/new_project.html', context)



# def display_page(request):
#     page = request.GET.get('page', 'home')
#     if not os.path.exists(f"{page}.html"):
#         return HttpResponseNotFound('Page not found')
#     return render(request, f"{page}.html")