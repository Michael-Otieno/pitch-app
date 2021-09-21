import os

# base_directory = os.path.abspath(os.path.dirname(__file__))
class Config(object):
    '''
    General configuration parent class
    '''
  
    class Config(object):
        '''
    General configuration parent class
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://pitch:1234@localhost/pitchproject'




class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

    

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}