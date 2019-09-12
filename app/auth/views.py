from . import auth
from flask import render_template,redirect,url_for
from .forms import RegForm
from .. import db
from ..models import User

@auth.route('/login')
def login():
    return render_template('auth/login.html')

@auth.route('/register',methods = ['POST','GET'])
def register():
    form = RegForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data, password = form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
        title = 'Create New Account'
    return render_template('auth/register.html',regform = form)