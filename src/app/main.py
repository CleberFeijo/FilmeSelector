from fastapi import FastAPI
from app.routes.api import router as FilmesRouter
from fastapi.middleware.cors import CORSMiddleware
from app.utils.settings import *

app = FastAPI(
    title='Filminhos',
    version='1.0',
    debug=settings.DEBUG
    )

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(FilmesRouter, tags=["Filmes"], prefix="/filmes")

@app.get("/", tags=["Root"])
async def read_root():
    raise Exception("Ocorreu um erro.")