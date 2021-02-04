import motor.motor_asyncio
from bson.objectid import ObjectId
from decouple import config

from datetime import datetime
from fastapi_users.db import MongoDBUserDatabase

from ..models.user import UserDB

MONGO_DETAILS = config('MONGO_DETAILS')
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.Boletin
aviso_collection = database.get_collection("aviso")


async def get_avisos(skip, limit):
    avisos = []
    collection = aviso_collection.find().skip(skip).limit(limit)
    async for aviso in collection:
        avisos.append(aviso_helper(aviso))
    return avisos


async def get_aviso_between_dates(vm):
    avisos = []
    async for aviso in aviso_collection.find():
        aviso = aviso_helper(aviso)
        fecha_aviso = datetime.strptime(aviso['fecha_aviso'], '%Y-%m-%d')
        if datetime.strptime(vm.fecha_desde, '%Y-%m-%d') < fecha_aviso < datetime.strptime(
                vm.fecha_hasta, '%Y-%m-%d'):
            avisos.append(aviso)
    return avisos


async def get_aviso(id: str) -> dict:
    aviso = await aviso_collection.find_one({"_id": ObjectId(id)})
    if aviso:
        return aviso_helper(aviso)


async def update_aviso(id: str, data: dict):
    if len(data) < 1:
        return False
    aviso = await aviso_collection.find_one({"_id": ObjectId(id)})

    if aviso:
        updated_aviso = await aviso_collection.update_one(
            {"_id": ObjectId(id)},
            {"$set": data}
        )
        if updated_aviso:
            return True
        return False


async def delete_aviso(id: str):
    aviso = await aviso_collection.find_one({"_id": ObjectId(id)})
    if aviso:
        await aviso_collection.delete_one({"_id": ObjectId(id)})
        return True


def aviso_helper(aviso) -> dict:
    return {
        "_id": str(aviso['_id']),
        "texto": aviso['texto'],
        "nro_boletin": aviso['nro_boletin'],
        "fecha_aviso": aviso['fecha_aviso'],
        "nro_aviso": aviso['nro_aviso'],
        "id_tipo_aviso": aviso['id_tipo_aviso'],
        "razon_social": aviso['razon_social'],
        "id_tipo_sociedad": aviso['id_tipo_sociedad'],
        "titulo": aviso['titulo'],
        "fechaConstitucion": aviso['fechaConstitucion'],
        "id_titulo": aviso['id_titulo'],
        "CUIT": aviso['CUIT'],
        "capitalSocial": aviso['capitalSocial'],
    }

