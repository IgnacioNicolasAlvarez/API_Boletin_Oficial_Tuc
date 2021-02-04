from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_users import FastAPIUsers
from fastapi_users.authentication import JWTAuthentication

from server.db.auth import user_db
from server.models.user import User, UserCreate, UserDB, UserUpdate
from server.routes.aviso import router as AvisoRouter
from server.routes.nlp import router as NlpRouter

SECRET = "SECRET"

auth_backends = []
jwt_authentication = JWTAuthentication(
    secret=SECRET, lifetime_seconds=3600,  tokenUrl="/auth/jwt/login")
auth_backends.append(jwt_authentication)


fastapi_users = FastAPIUsers(
    user_db,
    [jwt_authentication],
    User,
    UserCreate,
    UserUpdate,
    UserDB,
)


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(
    fastapi_users.get_auth_router(jwt_authentication),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_users_router(),
    prefix="/users",
    tags=["users"],
)




app.include_router(AvisoRouter, tags=["Aviso"], prefix="/aviso",
                   dependencies=[Depends(fastapi_users.get_current_active_user)])
                   
app.include_router(NlpRouter, tags=["NLP"], prefix="/nlp", )


@app.get("/", tags=["Root"], )
async def Saludar(user: User = Depends(fastapi_users.get_current_active_user)):
    return {"message": "Documentación en /docs"}
