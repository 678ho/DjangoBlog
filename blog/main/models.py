from django.db import models
# Create your models here.
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


class Write(models.Model) :
    title = models.CharField(max_length=100)
    contents = RichTextField()
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model) :
    blog = models.ForeignKey(Write, on_delete=models.CASCADE, null=True)
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_user = models.TextField(max_length=20)
    comment_thumbnail_url = models.TextField(max_length=300)
    comment_textfield = models.TextField()