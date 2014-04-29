

from google.appengine.ext import db
from framework.bottle import template, request
from framework.auth import Auth


def index():
    #pagina de inicio
    _auth = Auth() 
    if (_auth.is_login()):
        is_login = True
    else:
        is_login = False
    return template('home.html', {'is_login':is_login })


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
