class Config:
    """
    config parrent class

    """
    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
    SECRET_KEY = '<Flask WTF Secret Key>'

class ProdConfig(Config):
    """
    production config

    """
    pass
class DevConfig(Config):
    """

    """
    DEBUG = True