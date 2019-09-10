from flask import render_template
from . import main

@main.errorhandler(404)
def four_ow_four(error):
    """
    function to render 404 page

    """
    return render_template('error.html'),404