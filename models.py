
from google.appengine.ext import ndb


class Usuario(ndb.Model):
    name = ndb.StringProperty()


class Anime(ndb.Model):
    name = ndb.StringProperty()
    url = ndb.StringProperty()
    chapter_url = ndb.StringProperty()
    chapters = ndb.IntegerProperty()
    old_chapter = ndb.IntegerProperty()

