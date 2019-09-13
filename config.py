import os
from dotenv import load_dotenv
load_dotenv()
class Config:
    """
    config parrent class

    """
    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:mikey123@localhost/watchlist'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
class ProdConfig(Config):
    """
    production config

    """
    pass
class DevConfig(Config):
    """

    """
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}