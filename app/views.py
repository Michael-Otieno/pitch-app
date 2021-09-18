from flask import render_template
from app import app
from app.forms import LoginForm

#Views
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Michael'}
    title = 'Home'
    posts=[
        {
            'author':{'username':'John'},
            'body':'Beatiful day At home'
        },
        {
            'author':{'username':'Susan'},
            'body':'The movie was cool'
        }
    ]
 
    return render_template('index.html',title=title, user=user,posts=posts)

@app.route('/login')
def login():
    form = LoginForm()
    title = 'Sign In'
    return render_template('login.html',title=title,form=form)

