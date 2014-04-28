

from google.appengine.ext import db
from framework import bottle
from framework.bottle import template, request, response, redirect
from framework.auth import User, Auth


def registrar():
    """
        Registrar 
    """
    _auth = Auth()
    if not _auth.is_login():
        return template('auth/registrar.html')

    else:
        message = "Error ya has iniciado Session con la cuenta \"%s\" " %_auth.is_login()
        message += "en caso de querer proceder por fabor cierra la session actual."
        return template("message.html", {'message': message} )


def do_registrar():
    """
    """
    _auth = Auth()
    if not _auth.is_login:
        errors = [] #errores 
        #validacion de campos vacios
        _username = request.forms.get('username')
        if _username == "":
            errors.append("El campo Usuario esta vacio")

        #validacion de contrasenias
        _password = request.forms.get('password')
        repassword = request.forms.get('repassword')
        if len(_password) < 8 or len(_password) >= 16:
            errors.append("la contrasenia debe tener entre 8 y 16 caracteres")
        if _password != repassword:
            errors.append("Las contrasenias no coinciden")

        _name = request.forms.get('name')
        if _name == "":
            errors.append("El campo Nombre esta vacio")
        
        _email = request.forms.get('email')
        if _email == "":
            errors.append("El campo Email esta vacio")

        if len(errors) == 0:
            #validacion de que no exista el usuario
            query = db.GqlQuery("SELECT * FROM User WHERE username = :1", _username)        
            if query.count() != 0:
                errors.append("El nombre de usuarios \"%s\" ya existe" %_username)
                form_error = True

            else:            
                user = User(
                    username = _username,
                    password = _password,
                    name = _name,
                    email = _email,
                )
                user.put()
                return template("auth/registrar-ok.html")

        else:
            form_error = True
        #si llego hasta aqui hay algun tipo de errors        
        data = {
            "errors" : errors,
            "form_error": form_error,
            "username": _username,
            "name": _name,
            "email": _email,
        }
        return template("auth/registrar.html", data)

    else:
        message = "Error ya has iniciado Session con la cuenta \"%s\" " %_auth.is_login()
        message += "en caso de querer proceder por fabor cierra la session actual."
        return template("message.html", {'message': message} )


def login():
    """
        Iniciar Session
    """
    _auth = Auth()
    if not _auth.is_login():
        return template('auth/login.html')
    else:
        message = "Error ya has iniciado Session con la cuenta \"%s\" " %_auth.is_login()
        message += "en caso de querer proceder por fabor cierra la session actual."
        return template("message.html", {'message': message} )



def do_login():
    """
        Captura los datos de la vista para iniciar session
    """
    _auth = Auth()
    usr = request.forms.get('username')
    pwd = request.forms.get('password')

    if _auth.login(usr, pwd):
        redirect('/')
    else:
        return template('auth/login.html', {"error": True})


def logout():
    """
    Cerrar Session
    """
    response.delete_cookie("username", path="/")
    response.delete_cookie("is_admin", path="/")
    return template("auth/logout.html")



def listado():
    """
        Listado de Usuarios
        Nota: Requiere permiso administrado
    """
    users = db.GqlQuery("SELECT * FROM User")
    return template('auth/listado.html', {'users':users})

