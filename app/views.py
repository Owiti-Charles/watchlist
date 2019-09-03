from flask import render_template
from . import app
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    message = 'Hello Flask'
    return render_template('index.html',message = message)

@app.route('/movie/<int:id>')
def movie(id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    return render_template('movies.html',id = id)
