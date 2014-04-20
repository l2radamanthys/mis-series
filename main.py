
from framework import bottle
from framework.bottle import template
from framework.auth import User 

app = bottle.Bottle()

@app.get('/')
def index_page():
    #return template('home.html')
    return "Mis Series"

@app.get('/auth/registrar')
def user_registrar():
    return "Registrar"


@app.get('/auth/login')
def login():
    return template('auth/login.html')


# launch the App
bottle.debug(mode=True)
bottle.run(app=app, server="gae")






