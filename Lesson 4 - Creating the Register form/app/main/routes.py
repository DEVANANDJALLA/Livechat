from flask import render_template, request, session, redirect, url_for
from . import main
from .forms import LoginForm, RegisterForm

@main.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if request.method == 'GET':
        return render_template('index.html',form = form)


@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        print (form.email.data)
        session['email'] = form.email.data
        session['password'] = form.password.data
        return redirect(url_for('main.index'))
    elif request.method == 'GET':
        return render_template('register.html',form = form)
