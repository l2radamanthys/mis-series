
from framework.bottle import template, response, request
from framework.auth import Auth
from models import Serie, Chapter
from google.appengine.ext import db


def listado():
    _auth = Auth()
    if _auth.is_login():
        return template("series/listado.html")
    else:
        return template("sin-permisos.html")



def registrar():
    _auth = Auth()
    if _auth.is_login():
        return template("series/registrar.html")
    else:
        return template("sin-permisos.html")


def do_registrar():
    _auth = Auth()
    if _auth.is_login():
        #field validation
        _name = request.forms.get('name')
        _day = request.forms.get('day')
        _url = request.forms.get('url')
        _chapter_url = request.forms.get('chapter_url')
        _num_chapters = request.forms.get('mun_chapters')
        _old_chapter = request.forms.get('old_chapter')

        #el usuario existe se supone que esta logueado sino cagada jaaj
        _user = db.GqlQuery("SELECT * FROM User WHERE username = :1", _auth.is_login()).fetch(1)[0]
        
        if _num_chapters <= _old_chapter:
            _old_chapter = _num_chapters
            _enabled = False
        else:
            _enabled = True

        serie = Serie(
            user = _user,
            name = _name,
            day = _day,
            url = _url,
            chapter_url = _chapter_url,
            num_chapters = int(_num_chapters),
            old_chapter = int(_old_chapter), #ultimo capitulo que salio    
            enabled = _enabled
        )
        serie.put()
        n = int(_old_chapter) + 1
        #registro los capitulos
        for num in range(1, n):
            chapter = Chapter(
                serie = serie,
                number = num,
                url = serie.chapter_url %num,
                show = False
            )
            chapter.put()

        return "Serie Registrada"

        #return template("series/registrar.html")
    else:
        return template("sin-permisos.html")
   
