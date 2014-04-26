

from google.appengine.ext import db
from framework import bottle
from framework.bottle import template, request
from framework.auth import User, Auth

def registrar():
    _auth = Auth()
    usr = _auth.is_login()  
    if usr != False: #usuario logueado
        return "Error Usuario logueado %s" %usr
    else:
        return template('auth/registrar.html')


def do_registrar():
    _auth = Auth()
    usr = _auth.is_login()  
    if usr == False:
        user = User(
            username = request.forms.get('username'),
            password = request.forms.get('password'),
            name = request.forms.get('name'),
            email = request.forms.get('email'),
        )
        user.put()
        return "Usuario Registrado"
        #return template('auth/registrar.html')        
    else:    
        return "Error Usuario logueado %s" %usr


def login():
    """
        Iniciar Session
    """
    return template('auth/login.html')


def do_login():
    """
        Captura los datos de la vista para iniciar session
    """
    _auth = Auth()
    usr = request.forms.get('username')
    pwd = request.forms.get('password')
    
    
    return "Error vista no implementada" 


def listado():
    """
        Listado de Usuarios
        Nota: Requiere permiso administrado
    """
    users = db.GqlQuery("SELECT * FROM User")
    return template('auth/listado.html', {'users':users})

