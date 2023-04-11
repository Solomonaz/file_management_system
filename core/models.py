from django.db import models
# from datetime import datetime

class FileModel(models.Model):
    folder_name = models.CharField(max_length=100)
    folder = models.FileField(upload_to=' %m/%Y/folders/')
    created_at = models.DateTimeField()

    def formatted_date_created(self):
        return self.created_at.strftime('%d/%m/%Y')

    def __str__(self):
        return self.folder_name
    
    