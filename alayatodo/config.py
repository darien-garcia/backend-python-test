import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    
    SQLALCHEMY_DATABASE_URI ='sqlite:///' + os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
     + '\\tmp\\alayatodo.db') 
    SQLALCHEMY_TRACK_MODIFICATIONS = False