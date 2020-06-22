from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('movies/', views.MovieList.as_view(), name='movie_list'),
    path('movies/<int:pk>/', views.MovieDetail.as_view(), name='movie_detail'),
    path('movies/create', views.MovieCreate.as_view(), name='movie_create'),
]
