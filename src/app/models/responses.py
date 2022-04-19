from __future__ import annotations
from app.models.schemas import *

def ResponseModel(data: FilmesSchema, message) -> dict:
    return {
        "filme": data,
        "mensagem": message
    }

def ResponseModelMessage(message) -> dict:
    return {
        "mensagem": message
    }