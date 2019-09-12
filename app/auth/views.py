from . import auth
from flask import render_template,request,flash,redirect,url_for
from .forms import RegForm,LoginForm
from flask_login import login_user
from .. import db
from ..models import User

@auth.route('/login')
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or Password')
    title = 'Login'
    return render_template('auth/login.html',loginform = login_form, title = title)

    

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