from flask import render_template, redirect,request, url_for
from .requests import get_movies,get_movie,search_movie
from . import app
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    popular_movies = get_movies('popular')
    upcoming_movie = get_movies('upcoming')
    now_showing_movie = get_movies('now_playing')
    # print(popular_movies)
    title = 'Welcome To The Best Movie Online Movies Review Store'
    search_movie = request.args.get('movie_query')
    if search_movie:
        return redirect(url_for('search',movie_name = search_movie))
    else:
        return render_template('index.html',title = title, popular = popular_movies, upcoming = upcoming_movie, now_playing = now_showing_movie)

@app.route('/movie/<int:id>')
def movie(id):

    """
    View movie page function that returns the movie details page and its data
    """
    movie = get_movie(id)
    title = f'Your reviweing {id}'
    return render_template('movies.html', title = title, movie = movie)

@app.route('/search/<movie_name>')
def search(movie_name):
    """
    View to display search results 
    """
    movie_name_list = movie_name.split(" ")
    movie_name_format = "+".join(movie_name_list)
    searched_movie = search_movie(movie_name_format)
    title = f'Search Results for{movie_name}'
    return render_template('search.html', movies = searched_movie)
