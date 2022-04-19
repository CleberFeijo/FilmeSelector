from pymongo import MongoClient
from app.utils.settings import *

__all__ = 'collection',

local = settings.LOCAL
clientlocal = MongoClient(local)
database = clientlocal.movies
collection = database.get_collection("filminhos")