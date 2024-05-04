from django.db import models
from django import forms
import os

# Create your models here.
def validate_file(dataset_file):
    if dataset_file.name.endswith(".csv") or dataset_file.name.endswith(".txt"):
        if str(dataset_file.file).endswith(".txt"):
            dataset_file = str(dataset_file.file).replace(".txt", ".csv")
        
        if os.path.exists(f"media/{dataset_file}"):
            raise forms.ValidationError("File already exist in the server!\nContact Admin!")
        
        has_data = FileUploaded.objects.filter(file = f"media/{dataset_file}")
        if has_data.exists():
            raise forms.ValidationError("File already exist in the database!\nContact Admin!")
    else:
        raise forms.ValidationError("Not a txt/csv file!")
class FileUploaded(models.Model):
    file = models.FileField(upload_to="media", validators=[validate_file], unique=True)

    def __str__(self) -> str:
        return self.file