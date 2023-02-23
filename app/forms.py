from .models import ModelTask
from django import forms


class Formtask(forms.ModelForm):
    class Meta:
        model = ModelTask
        fields = '__all__'
    
    def __init__(self, *args, **kargs):
        super(Formtask, self).__init__(*args, **kargs)
        self.fields['task_name'].widget.attrs={'placeholder':'Add new task ...', 'class':'border border-primary border-1 form-control form-control-lg me-3'}
        self.fields['status'].widget.attrs={'class':'border border-primary form-control-lg text-muted border-1'}
        self.fields['user'].widget.attrs={'class':'border border-primary form-control-lg text-muted border-1'}