
from fastapi import APIRouter, Body, Depends
from pydantic import BaseModel, Field

import spacy

router = APIRouter()


class Mensaje(BaseModel):
    texto: str


@router.post("/entidades", response_description="NLP data retrieved")
async def get_entidades_from_texto(mensaje: Mensaje):
    nlp = spacy.load("es_core_news_sm")
    entidades = []

    doc = nlp(mensaje.texto.lower())

    for token in doc:
        if token.tag_ == "PROPN" and token.pos_ == "PROPN" and token.shape_ == 'Xxxxx': 
            entidades.append(token)

    texto = ' '.join(str(e) for e in entidades)

    return {
        "Entidades": entidades,
        "Mensaje Resultante": texto,
        "Mensaje Inicial": mensaje.texto,
    }
