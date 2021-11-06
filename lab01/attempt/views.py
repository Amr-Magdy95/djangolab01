from django.shortcuts import redirect, render
from django.http import HttpResponse

my_context = {
    "movies": [
        { "idx": 0, "id": 1,"Name": "Pan's Labyrinth", "Director": "Guillermo Del Toro", "Release_Year": "2000ish"},
        { "idx": 1, "id": 2,"Name": "Fight Club", "Director": "Some Guy", "Release_Year": "1999"},
        { "idx": 2, "id": 3,"Name": "FullMetal Jacket", "Director": "Stanley Kubrick", "Release_Year": "1980ish"}
        
        ],
    "worked": True
}  

def _get_target_movie(target_id):
    # Filter the list based on the task id sent and compare it toward each dictionary item in the list
    index_of_task = -1
    res = []
    for movie in my_context["movies"]:
        if target_id == movie.get("id"):
            res = movie 
    print(res)

    # Getting index of the required task from my_task_list
    index_of_movie = res.get("idx")

    print("idx : {}".format(index_of_movie) )
    return index_of_movie


def list_movies(request, *args, **kwargs):
    _get_target_movie(2)
    return render(request, 'attempt/list_movies.html', context=my_context)


def movie_details(request, *args, **kwargs):
    movie_id = kwargs.get('movie_id')


    movie_index = _get_target_movie(movie_id)
    print("movie id : {}, movie_index: {}".format(movie_id, movie_index))

    movie_dict = my_context["movies"][movie_index]

    res = {
        'movie_id': movie_dict.get('id'),
        'Movie_Name': movie_dict.get('Name'),
        'Director': movie_dict.get('Director'),
        'Release_Year': movie_dict.get('Release_Year')
    }

    print(res)
    return render(request, 'attempt/movie_details.html', context=res)
    #return HttpResponse("Here")

#
#    return render(request, 'todo/todo_detail.html', context=my_context)

def movie_update(request, *args, **kwargs):
    movie_id = kwargs.get('movie_id')
    index_to_update = _get_target_movie(movie_id)
    movie_dict = my_context["movies"][index_to_update]["Name"] = 'Reanimated {}'.format(my_context["movies"][index_to_update].get("Name"))
    print(movie_dict)

    return redirect('../../../attempt/index')

def movie_delete(request, *args, **kwargs):
    movie_id = kwargs.get('movie_id')
    index_to_delete = _get_target_movie(movie_id)

    if my_context:
        my_context["movies"].pop(index_to_delete)
    
    return redirect('../../../attempt/index')

    

