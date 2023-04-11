from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_folder/', views.add_folder, name='add_folder'),
    # path('search/', views.search, name='search'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('download/<int:id>/', views.download, name='download'),
]
