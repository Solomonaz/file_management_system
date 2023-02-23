from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('search/', views.search, name='search')
    
]