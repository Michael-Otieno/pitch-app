from flask import render_template
from . import main
from flask_login import login_required


#Views
@main.route('/')

def index():
   
    return render_template('index.html')



@main.route('/user/<uname>/update', methods=['GET', 'POST'])
@login_required
def update_profile(uname):
    
    return render_template('profile/update.html')
