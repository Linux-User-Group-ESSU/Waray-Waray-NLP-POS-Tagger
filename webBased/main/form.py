from django import forms
from .models import *

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = FileUploaded
        fields = ['file']
        widgets = {
            'file' : forms.FileInput(attrs={
                'accept' : '.txt,.csv',
                'onchange' : 'uploadFile()'
            })
        }