from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Movie
from .forms import ViewingForm


# Create your views here.
def home(request):
    return render(request, 'home.html', {'title': 'Movies Home'})


# ---------------------------MOVIES-------------------------------- #

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
    
    def get_context_data(self):
        context = super().get_context_data()
        context['title'] = 'Add A Movie'
        return context

    def form_valid(self, form):
        return super().form_valid(form)
    
    
class MovieUpdate(UpdateView):
    model = Movie
    fields = '__all__'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update ' + context['movie'].title 
        return context
    
    
class MovieDelete(DeleteView):
    model = Movie
    success_url = '/movies/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete ' + context['movie'].title 
        return context
    
    
# ---------------------------VIEWINGS-------------------------------- #


def add_viewing(request, movie_id):
    form = ViewingForm(request.POST)
    if form.is_valid():
        new_viewing = form.save(commit=False)
        new_viewing.movie_id = movie_id
        new_viewing.save()
    return redirect('movie_detail', movie_id=movie_id)