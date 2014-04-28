
from bottle import request, response
from google.appengine.ext import db

#clave para codificar las cookies
SECRET_KEY = "hola123"


class User(db.Model):
    username = db.StringProperty()
    password = db.StringProperty()
    name = db.StringProperty()
    email = db.EmailProperty()
    is_super = db.BooleanProperty(default=False)



class Auth:
    def login(self, username, password):
        query = db.GqlQuery("SELECT * FROM User WHERE username = :1 AND password = :2", username, password)
        if (query.count() == 1):
            user = query[0]
            response.set_cookie('username', username, secret=SECRET_KEY, path="/")
            response.set_cookie('is_admin', str(user.is_super), secret=SECRET_KEY, path="/")
            return True

        else:
            return False


    def is_login(self):
        """
            Consulta si hay un usuario logueado, en caso que si retornara su
            nombre de usuario, caso contrario devolvera False
        """
        user = request.get_cookie('username', secret=SECRET_KEY)
        if user != None:
            return user
        else:
            return False


    def is_admin(self):
        adm = request.get_cookie('is_admin', secret=SECRET_KEY)
        return adm


    def logout():
        pass



