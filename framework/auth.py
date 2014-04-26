
from bottle import request
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
        query = db.GqlQuery("SELECT * FROM User WHERE username = :1", username)
        user = query[0]
        pass

        request.set_cookie('username', username, secret=SECRET_KEY)
        request.set_cookie('is_admin', user.is_super, secret=SECRET_KEY)
        


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
        pass


    
    


