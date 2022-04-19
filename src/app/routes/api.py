from __future__ import annotations
from fastapi import APIRouter, Depends
from typing import *

from app.requests import (
    requests_filme,
    insert_filme
)
from app.models.params import (
    ParamsModel,
)
from app.models.responses import (
    ResponseModel,
    ResponseModelMessage,
)

router = APIRouter()

@router.post("/adicionar", response_description="Adiciona um filme ao banco de dados")
def post_add_filme(params: ParamsModel = Depends()):
    try:
        print(params.modelo)
        filme = {
            'nome': params.nome,
            'plataforma': params.plataforma,
            'tipo': params.tipo,
            'modelo': params.modelo,
            'nota_imdb': params.nota_imdb
        }
        response = insert_filme(filme)
        if response:
            return ResponseModelMessage(response)
        return ResponseModelMessage("O filme não pôde ser adicionado")
    except Exception as error:
        raise error

@router.get("/assistir", response_description="Retorna qual filme devemos assistir")
def get_filme():
    try:
        response = requests_filme()
        if response:
            return ResponseModel(response, "Esse é o filme que vamos assistir hoje")
        return ResponseModelMessage("Ocorreu algum erro ao retornar o filme :(")
    except Exception as error:
        raise error