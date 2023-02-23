from django import forms
from . models import Project_List

class ProjectListForm(forms.ModelForm):
    class Meta:
        model = Project_List
        # fields = ['name','description','status','start_date','end_date','users']
        fields = '__all__'
    
    def __init__(self, *args, **kargs):
        super(ProjectListForm, self).__init__(*args, **kargs)
        self.fields['name'].widget.attrs={'class':'form-control form-control-sm'}
        self.fields['description'].widget.attrs={'class':'form-control', 'cols':"30", 'rows':"10"}
        self.fields['status'].widget.attrs={'class':'form-control form-control-sm custom-select custom-select-sm'}
        self.fields['start_date'].widget.attrs={'class':' form-control form-control-sm'}
        self.fields['end_date'].widget.attrs={'class':' form-control form-control-sm'}
        # self.fields['status'].widget.attrs={'class':' form-control-sm'}
        # self.fields['status'].widget.attrs={'class':' form-control-sm'}
        self.fields['users'].widget.attrs={'class':' form-control form-control-sm'}