
from framework import bottle


import views
import auth_views
import series_views


def routing(app):
    """
        Define la ruta de las diferentes aplicaciones
    """
    app.route('/',                  ['GET'],    views.index)
    app.route('/access-denied',                  ['GET'],    views.access_denied)
    app.route('/debug',             ['GET'],    views.debug)

    #Session
    app.route('/auth/registrar',    ['GET'],    auth_views.registrar)
    app.route('/auth/registrar',    ['POST'],   auth_views.do_registrar)
    app.route('/auth/login',        ['GET'],    auth_views.login)
    app.route('/auth/login',        ['POST'],   auth_views.do_login)
    app.route('/auth/logout',       ['GET'],    auth_views.logout)
    app.route('/auth/listado',      ['GET'],    auth_views.listado)

    app.route('/series/listado',    ['GET'],    series_views.listado)
    app.route('/series/registrar',  ['GET'],    series_views.registrar)
    app.route('/series/registrar',  ['POST'],   series_views.do_registrar)
    #app.route('/series/',    ['GET'],    series_views.)



app = bottle.Bottle()
routing(app)
# launch the App
bottle.debug(mode=True)
bottle.run(app=app, server="gae")






