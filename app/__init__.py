from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap

app = Flask(__name__, instance_relative_config = True)
app.config.from_object(DevConfig)
app.config.from_pyfile("config.py")

bootstrap = Bootstrap(app)

from app import views 
from app import error
 