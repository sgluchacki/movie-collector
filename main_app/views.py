from django.shortcuts import render, redirect
from .models import Movie
from django.views.generic import ListView, DetailView


# Create your views here.
def home(request):
    return render(request, 'home.html', {'title': 'Movies Home'})

# MOVIES

class MovieList(ListView):
    model = Movie
    
    def get_context_data(self):
        context = super().get_context_data()
        context['title'] = 'Movies List'
        return context

class MovieDetail(DetailView):
    model = Movie
    pk_url_kwarg = 'movie_id'
    
    def get_context_data(self, movie_id=movie_id):
        movie = Movie.objects.get(id=movie_id)
        context = super().get_context_data()
        context['title'] = movie.title + ' Details'
        return context