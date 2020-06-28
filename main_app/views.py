from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Movie, Cast
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
    

# class MovieDetail(DetailView):
#     model = Movie
#     # pk_url_kwarg = 'movie_id'
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = context['movie'].title + ' Details'
#         context['viewing_form'] = ViewingForm()
#         context['cast'] = Cast.objects.filter(movie=self)
#         context['all_cast'] = Cast.objects.all()
#         return context

def movie_detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    available_cast = Cast.objects.exclude(id__in = movie.cast.all().values_list('id'))
    context = {
        'title': movie.title + ' Details',
        'available_cast': available_cast,
        'movie': movie,
        'viewing_form': ViewingForm(),
    }
    return render(request, 'main_app/movie_detail.html', context)
    
    
class MovieCreate(CreateView):
    model = Movie
    fields = ['title', 'year_of_release', 'art_image_url']
    
    def get_context_data(self):
        print(self, 'self in MovieCreate')
        context = super().get_context_data()
        context['title'] = 'Add A Movie'
        context['cast'] = Cast.objects.all()
        return context

    def form_valid(self, form):
        return super().form_valid(form)
    
    
class MovieUpdate(UpdateView):
    model = Movie
    fields = ['title', 'year_of_release', 'art_image_url']
    
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


def add_viewing(request, pk):
    form = ViewingForm(request.POST)
    if form.is_valid():
        new_viewing = form.save(commit=False)
        new_viewing.movie_id = pk
        new_viewing.save()
    return redirect('movie_detail', movie_id=pk)


# -----------------------------CAST---------------------------------- #

class CastCreate(CreateView):
    model = Cast
    fields = '__all__'
    
    def get_context_data(self):
        context = super().get_context_data()
        context['title'] = 'Add A Cast Member'
        return context

    # def form_valid(self, form):
    #     return super().form_valid(form)
    
class CastList(ListView):
    model = Cast
    
    def get_context_data(self):
        context = super().get_context_data()
        context['title'] = 'Cast List'
        return context
    
def assoc_cast_member(request, movie_id, cast_id):
    Movie.objects.get(id=movie_id).cast.add(cast_id)
    return redirect('movie_detail', movie_id=movie_id)

def unassoc_cast_member(request, movie_id, cast_id):
    Movie.objects.get(id=movie_id).cast.remove(cast_id)
    return redirect('movie_detail', movie_id=movie_id)