from flask import render_template
from . import app
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Welcome To The Best Movie Online Movies Review Store'
    return render_template('index.html',title = title)

@app.route('/movie/<int:id>')
def movie(id):

    """
    View movie page function that returns the movie details page and its data
    """
    title = f'Your reviweing {id}'
    return render_template('movies.html', title = title)
