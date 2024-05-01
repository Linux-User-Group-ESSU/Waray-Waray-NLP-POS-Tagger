from django.db import models
from django import forms
import os

# Create your models here.
def validate_file(voter_file):
    if voter_file.name.endswith(".csv") or voter_file.name.endswith(".txt"):
        if os.path.exists(f"media/{voter_file}"):
            raise forms.ValidationError("File already exist in the database!")
    else:
        raise forms.ValidationError("Not a txt/csv file!")
class FileUploaded(models.Model):
    file = models.FileField(upload_to="media", validators=[validate_file], unique=True)

    def __str__(self) -> str:
        return self.file