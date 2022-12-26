from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import DateTimeField

# Create your models here.


class Article(models.Model):
    title = models.TextField(max_length = 100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)