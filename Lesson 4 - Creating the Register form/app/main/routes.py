from flask import render_template,request
from . import main
from .forms import LoginForm

@main.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if request.method == 'GET':
        return render_template('index.html',form = form)
