
from google.appengine.ext import db
from framework import bottle
from framework.bottle import template, request
from framework.auth import User, Auth

app = bottle.Bottle()

@app.get('/')
def index_page():
    return template('home.html')
    

@app.get('/auth/registrar')
def user_add():
    _auth = Auth()
    usr = _auth.is_login()  
    if usr != False: #usuario logueado
        return "Error Usuario logueado %s" %usr
    else:
        return template('auth/registrar.html')


@app.post('/auth/registrar')
def do_user_add():
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


@app.get('/auth/login')
def login():
    return template('auth/login.html')
    

#debug view
@app.get('/debug')
def debug():
    a = db.GqlQuery("SELECT * FROM User")
    t = ""
    for e in a:
        t = t + "<p>(%s, %s, %s, %s, %s)</p>" %(e.username, e.password, e.name, e.email, e.is_super)
    #a = User.get()
    return t





# launch the App
bottle.debug(mode=True)
bottle.run(app=app, server="gae")






