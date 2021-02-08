
import spacy
from fastapi import APIRouter, Body, Depends
from pydantic import BaseModel, Field
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

MODEL_URL = "mrm8488/distill-bert-base-spanish-wwm-cased-finetuned-spa-squad2-es"

router = APIRouter()


class Mensaje(BaseModel):
    texto: str


class Consulta(BaseModel):
    pregunta: str
    texto: str


@router.post("/entidades", response_description="NLP data retrieved")
async def get_entidades_from_texto(mensaje: Mensaje):
    nlp = spacy.load("es_core_news_sm")
    entidades = []

    doc = nlp(mensaje.texto[11:])

    for token in doc:
        if token.tag_ == "PROPN" and token.pos_ == "PROPN" and len(token.shape_) >= 4:
            entidades.append(token.text)
        # entidades.append(
        #    {token.text: {"tag": token.tag_, "pos": token.pos_, "shape": token.shape_}})

    return {
        "Entidades": entidades,
        "Mensaje Resultante": ' '.join(str(e) for e in entidades),
        "Mensaje Inicial": mensaje.texto,
    }


@router.post("/entidades", response_description="NLP data retrieved")
async def get_entidades_from_texto(consulta: Consulta):
    tokenizer = AutoTokenizer.from_pretrained(MODEL_URL, do_lower_case=False)
    model = AutoModelForQuestionAnswering.from_pretrained(MODEL_URL)

    nlp = pipeline('question-answering', model=model, tokenizer=tokenizer)
    salida = nlp({'question': consulta.pregunta, 'context': consulta.texto})

    return {
        "Mensaje Inicial": consulta.texto,
        "Respuesta": salida['answer'],
        "Puntaje": salida['score'],
    }
