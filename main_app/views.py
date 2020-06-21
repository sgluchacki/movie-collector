from django.shortcuts import render, redirect
from .models import Movie
from django.views.generic import ListView


# Create your views here.
def home(request):
    return render(request, 'home.html', {'title': 'Movies Home'})

# MOVIES

class MovieList(ListView):
    model = Movie
    
    def get_context_data(self):
        context = super().get_context_data()
        context['title'] = 'Movies'
        return context