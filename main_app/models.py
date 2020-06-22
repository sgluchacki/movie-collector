from django.db import models
from django.urls import reverse
import datetime


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    year_of_release = models.IntegerField(default=datetime.date.today().year)
    art_image_url = models.URLField(max_length=2000)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('movie_detail', kwargs={'pk': self.id})


class Viewing(models.Model):
    date = models.DateField(
        default=datetime.date.today()
        )
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)