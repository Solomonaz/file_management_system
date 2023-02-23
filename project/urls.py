from django.shortcuts import HttpResponse
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('report/', views.report, name='report'),
    path('project_list/', views.project_list, name='project_list'),
    path('new_project/', views.new_project, name='new_project'),
    path('del_project/<int:id>', views.del_project, name='del_project'),
    path('edit_project/<int:id>', views.edit_project, name='edit_project'),
]