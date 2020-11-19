import motor.motor_asyncio
from bson.objectid import ObjectId
from decouple import config

MONGO_DETAILS = config('MONGO_DETAILS')


async def retrieve_avisos():
    avisos = []
    async for aviso in aviso_collection.find():
        avisos.append(aviso_helper(aviso))
    return avisos


async def retrieve_aviso(id: str) -> dict:
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


client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.Boletin

aviso_collection = database.get_collection("aviso")


def aviso_helper(aviso) -> dict:
    return {
        "_id": aviso['_id'],
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
