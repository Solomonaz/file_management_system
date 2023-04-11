from django import forms
from . models import FileModel

class FileForm(forms.ModelForm):
    class Meta:
        model = FileModel
        fields = ['folder_name','folder', 'created_at']

        widgets = {
            'created_at': forms.DateInput(format='%d/%m-%Y'),
        }
