from django.contrib import admin
from django.urls import path, include
from attempt import views

app_name = 'attempt'


urlpatterns = [
    #Experimental
    #path('', views.table, name="table"),
    #path('detail/<int:task_id>', views.attempt_detail, name="table"),
    #path('<int:task_id>', views.movie_detail, name="todo-detail"),
    #View Movies
    path('index', views.list_movies, name="list_movies"),
    #C
    #R
    path('movie/<int:movie_id>/view', views.movie_details, name='movie-details'),
    #U
    path('movie/<int:movie_id>/update', views.movie_update, name='movie-update'),
    #D
    path('movie/<int:movie_id>/delete', views.movie_delete, name='movie-delete'),
  ]