from django.db import models

# Create your models here.
class FileUploaded(models.Model):
    file = models.FileField(upload_to="read")