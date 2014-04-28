

from google.appengine.ext import db
from framework.bottle import template, request
from framework.auth import Auth


def index():
    #pagina de inicio
    return template('home.html')



def access_denied():
    """
        Vista que se mostrara cuando el usuario no tenga los permisos suficientes
        normalmente sera por no haber iniciado session
    """
    return template('sin-permisos.html')



def debug():
    """
        Vista Para Pruebas
    """
    a = Auth()
    return str(a.is_login()),'-', str(a.is_admin())
