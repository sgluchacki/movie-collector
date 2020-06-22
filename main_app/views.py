from django.shortcuts import render, redirect
from .models import Movie
from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, UpdateView, DeleteView


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
    # pk_url_kwarg = 'movie_id'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['movie'].title + ' Details'
        return context
    
    
class MovieCreate(CreateView):
    model = Movie
    fields = '__all__'

    def form_valid(self, form):
        return super().form_valid(form)
    
    
class MovieUpdate(UpdateView):
    model = Movie
    fields = '__all__'