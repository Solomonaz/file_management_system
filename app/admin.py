from django.contrib import admin
from .models import ModelTask


class AdminTask(admin.ModelAdmin):
    list_display = ('task_name', 'status','created_at')
admin.site.register(ModelTask, AdminTask)