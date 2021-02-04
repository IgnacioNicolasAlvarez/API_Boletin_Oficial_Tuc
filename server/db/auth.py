import motor.motor_asyncio
from decouple import config
from fastapi_users.db import MongoDBUserDatabase

from ..models.user import UserDB

MONGO_DETAILS = config('MONGO_DETAILS')
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.Boletin
usuarios_collection = database.get_collection("usuarios")

user_db = MongoDBUserDatabase(UserDB, usuarios_collection)
