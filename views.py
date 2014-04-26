

from google.appengine.ext import db
from framework.bottle import template, request


def index():
    #pagina de inicio
    return template('home.html')


def debug():
    """
        Vista Para Pruebas
    """
    return "Hello World"
