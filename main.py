from fastapi import FastAPI
from server.routes.aviso import router as AvisoRouter

app = FastAPI()

app.include_router(AvisoRouter, tags=["Aviso"], prefix="/aviso")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}
