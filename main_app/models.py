from django.db import models
from django.urls import reverse
from django.utils import timezone
import datetime


class Cast(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('cast_list')
    
    
class Movie(models.Model):
    title = models.CharField(max_length=100)
    year_of_release = models.IntegerField(default=datetime.date.today().year)
    art_image_url = models.URLField(max_length=2000)
    cast = models.ManyToManyField(Cast)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('movie_detail', kwargs={'movie_id': self.id})


class Viewing(models.Model):
    date = models.DateField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)