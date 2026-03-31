import os

class Config:
    DEBUG = os.environ.get('FLASK_ENV') == 'development'
    DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///app.db')