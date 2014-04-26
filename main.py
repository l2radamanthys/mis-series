
from framework import bottle

import views
import auth_views    


def routing(app):
    """
        Define la ruta de las diferentes aplicaciones
    """
    app.route('/',                  ['GET'],    views.index)
    app.route('/debug',             ['GET'],    views.debug)

    #Session
    app.route('/auth/registrar',    ['GET'],    auth_views.registrar)
    app.route('/auth/registrar',    ['POST'],   auth_views.do_registrar)
    app.route('/auth/login',        ['GET'],    auth_views.login)
    app.route('/auth/login',        ['POST'],   auth_views.do_login)
    app.route('/auth/listado',      ['GET'],    auth_views.listado)




app = bottle.Bottle()
routing(app)
# launch the App
bottle.debug(mode=True)
bottle.run(app=app, server="gae")






