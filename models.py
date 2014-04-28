
from google.appengine.ext import db
from framework.auth import User


class Serie(db.Model):
    user = db.ReferenceProperty(User) #Fk
    name = db.StringProperty()
    url = db.StringProperty() 
    day = db.StringProperty() #dia que sale
    chapter_url = db.StringProperty()
    num_chapters = db.IntegerProperty() #numero de capitulos
    old_chapter = db.IntegerProperty() #ultimo capitulo que salio
    create = db.DateProperty(auto_now_add=True)
    update = db.DateProperty(auto_now=True)
    enabled = db.BooleanProperty() #estado la serie define si se actualizara o no
    #se crea una referencia adicional para invocar todos los capitulos
    #chapters


class Chapter(db.Model):
    serie = db.ReferenceProperty(Serie, collection_name="chapters") 
    number = db.IntegerProperty()
    url =  db.StringProperty()
    show = db.BooleanProperty()  #fue visto
