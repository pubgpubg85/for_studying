from django.contrib import admin
from django.db import models


class Dbns(models.Model):
    document_name = models.CharField(max_length=200)
    document_file = models.FileField(upload_to='dbns/')

    def __str__(self):
        return self.document_name
