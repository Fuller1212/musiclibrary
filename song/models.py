
from django.db import models
from django.forms import CharField, DateField

# Create your models here.


class Song(models.Model):
    title = models.CharField(max_length=300)
    artist = models.CharField(max_length=300)
    album = models.CharField(max_length=300)
    release_date = models.DateField()
    genre = models.CharField(max_length=300)
    like = models.IntegerField(default=0)