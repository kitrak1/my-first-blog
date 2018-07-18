from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
from django.urls import reverse


class About(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()

    def __str__(self):
        return self.title


class Services(models.Model):
    title1 = models.CharField(max_length=200)
    title2 = models.TextField(max_length=200)
    content = RichTextField()

    def __str__(self):
        return self.title1
