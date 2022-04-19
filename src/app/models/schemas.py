from __future__ import annotations
from datetime import datetime
from typing import Optional
from bson import ObjectId
from pydantic import BaseModel, Field

class FilmesSchema(BaseModel):
    nome: str = Field(...)
    plataforma: str = Field(...)
    tipo: str = Field(...)
    modelo: str = Field(...)
    nota_imdb: float = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "nome": "Ataque dos cães",
                "plataforma": "Netflix",
                "tipo": "Drama",
                "modelo": "Filme",
                "nota_imdb": 6.9,
            }
        }