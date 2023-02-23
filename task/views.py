from django.shortcuts import render
from django.http import HttpResponse


def task(request):
    return render(request, 'pages/task.html')