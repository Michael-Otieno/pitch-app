from flask import render_template,flash,redirect,url_for
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

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    title = 'Sign In'
    if form.validate_on_submit():
        return redirect(url_for('index'))
    
    return render_template('login.html',title=title,form=form)

