from __future__ import annotations
from typing import Optional
from app.utils.pydantic_utils import ModelModelo, ModelTipo
from pydantic import BaseModel

class ParamsModel(BaseModel):
    nome: str
    plataforma: str
    tipo: ModelTipo
    modelo: ModelModelo
    nota_imdb: float