from django.contrib import admin
from . models  import FileModel


class FileAdmin(admin.ModelAdmin):
    list_display = ('folder_name', 'folder', 'created_at')


admin.site.register(FileModel, FileAdmin)