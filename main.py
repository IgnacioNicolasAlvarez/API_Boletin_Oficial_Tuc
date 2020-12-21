from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from server.routes.aviso import router as AvisoRouter

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(AvisoRouter, tags=["Aviso"], prefix="/aviso")


@app.get("/", tags=["Root"])
async def Saludar():
    return {"message": "Documentación en /docs"}
