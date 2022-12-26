from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=20)
    audience = models.TextField()
    release_data = models.DateTimeField(auto_now_add=True)
    genre = models.DateTimeField(auto_now=True)
    score = models.DateTimeField(auto_now=True)
    poster_utl = models.DateTimeField(auto_now=True)
    description = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title