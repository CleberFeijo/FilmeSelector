from bson import ObjectId
from enum import Enum

class ModelModelo(str, Enum):
    filme = "Filme"
    serie = "Série"
    dorama = "Dorama"
    animacao = "Animação"

class ModelTipo(str, Enum):
    terror = "Terror"
    comedia = "Comédia"
    acao = "Ação"
    drama = "Drama"
    romance = "Romance"
    suspense = "Suspense"
    ficcao = "Ficção"