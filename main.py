
from framework import bottle
from framework.bottle import template
from framework.auth import User 

app = bottle.Bottle()

@app.get('/')
def index_page():
    return template('home.html')

@app.get('/usuario/registrar')
def registrar_page():
    return "Registrar"


# launch the App
bottle.debug(mode=True)
bottle.run(app=app, server="gae")






