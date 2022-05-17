from flask import render_template,redirect,request,url_for,flash
from . import auth
from ..models import User
from .forms import LoginForm,SignupForm
from flask_login import login_user,logout_user,login_required
from ..import db
from ..email import mail_message

@auth.route('/signup',methods = ['GET','POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        user = User(username = form.username.data,email = form.email.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()
        #mail_message("You can now login")
        return redirect(url_for('auth.login'))
    title = "Sign up to The House of Elegance Blog"
    return render_template('auth/signup.html',title=title, form = form)


@auth.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user,form.remember_me.data)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('main.index')
            return redirect(next)

        flash('Invalid username or password')

    title = "The House of Elegance Blog login"
    return render_template('auth/login.html',form=form,title=title)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for("main.index"))