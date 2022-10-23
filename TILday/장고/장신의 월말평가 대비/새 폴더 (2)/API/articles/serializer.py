from rest_framework import serializers
from .models import * 

class Meta:
    model = Article
    fields = ('id', 'title', 'content')