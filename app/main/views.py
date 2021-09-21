from flask import render_template
from . import main


#Views
@main.route('/')

def index():
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
 
    return render_template('index.html',title=title,posts=posts)



@main.route('/register', methods=['GET', 'POST'])
def register():
    
    return render_template('register.html', title='Register')
