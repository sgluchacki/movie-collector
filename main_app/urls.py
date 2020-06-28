from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('movies/', views.MovieList.as_view(), name='movie_list'),
    path('movies/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    # path('movies/<int:pk>/', views.MovieDetail.as_view(), name='movie_detail'),
    path('movies/create/', views.MovieCreate.as_view(), name='movie_create'),
    path('movies/<int:pk>/update/', views.MovieUpdate.as_view(), name='movie_update'),
    path('movies/<int:pk>/delete/', views.MovieDelete.as_view(), name='movie_delete'),
    path('movies/<int:pk>/add_viewing/', views.add_viewing, name='add_viewing'),
    path('cast/', views.CastList.as_view(), name='cast_list'),
    path('cast/create', views.CastCreate.as_view(), name='cast_create'),
    path('movies/<int:movie_id>/assoc_cast_member/<int:cast_id>', views.assoc_cast_member, name='cast_assoc'),
    path('movies/<int:movie_id>/unassoc_cast_member/<int:cast_id>', views.unassoc_cast_member, name='cast_unassoc'),
]
