from __future__ import annotations
from app.database.colection import *
from app.models.schemas import FilmesSchema
from random import randrange

def requests_filme():
    try:
        filmes = list(collection.find({}))
        random = randrange(0, len(filmes))
        for count, filme in enumerate(filmes):
            if count == random:
                return filmes[filme]
    except Exception as error:
        raise error

def insert_filme(filme: FilmesSchema):
    try:
        response = collection.insert_one(filme)
        if response:
            return "Filme inserido com sucesso"
    except Exception as error:
        raise error