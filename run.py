from app import app, db
from app.models import User, Pitch

@app.shell_context_processor
def make_shell_context():
    return {'db':db, 'User':User, 'Pitch':Pitch}

if __name__=='__main__':
    app.run(debug=True)