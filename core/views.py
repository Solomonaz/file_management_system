from django.shortcuts import render, redirect, HttpResponseRedirect
from . models import FileModel
from . forms import FileForm
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.core.paginator import Paginator

def index(request):
    search_data = request.GET.get('search')
    if search_data:
        datas = FileModel.objects.filter(Q(folder_name__icontains=search_data) | Q(created_at__icontains=search_data))
    else:
        datas = FileModel.objects.all().order_by('-created_at')
    
    paginator =  Paginator(datas, 6) #get 10 item per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'datas':datas,
        'page_obj':page_obj,
    }
    return render(request, 'index.html', context)

def add_folder(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            folder_name = form.cleaned_data['folder_name']
            folder = form.cleaned_data['folder']
            created_at = form.cleaned_data['created_at']

            new_folder  = FileModel.objects.create(folder_name=folder_name, folder=folder, created_at=created_at)
            new_folder.save()
            return redirect('index')
    else:
        form = FileForm()
    
    context = {
        'form':form,
    }
    return render(request, 'add_folder.html', context) 

def delete(request, id):
    delete_item = FileModel.objects.get(id=id)
    delete_item.delete()
    return redirect('index')
@csrf_exempt
def download(request, id):
    uploaded_file = get_object_or_404(FileModel, id=id)
    file_path = uploaded_file.folder.path
    try:
        with open(file_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/octet-stream')
            response['Content-Disposition'] = 'attachment; filename=' + uploaded_file.folder.name.split('/')[-1]
            return response
    except FileNotFoundError:
        raise Http404("File not found")
# def search(request):
#     search_data = request.GET.get('search')
#     if search_data:
#         data = FileModel.objects.filter(Q(folder_name___icontains=search_data) | Q(created_at__icontains=search_data))
#     else:
#         data = FileModel.objects.all().order_by('-created_at')

#     return render(request, 'index.html',{'data':data})