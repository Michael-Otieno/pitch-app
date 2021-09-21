from flask import Flask
from config import config_options #Config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



def create_app(config_name):

    #Initializing application
    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    #Registering a blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #Initializing flask extensions
    db.init_app(app)
    
    return app

# from app import views, models,errors