from fastapi import APIRouter, Body

from server.database import (
    delete_aviso,
    retrieve_aviso,
    retrieve_avisos,
    update_aviso,
    retrieve_aviso_between_dates
)
from server.models.aviso import (
    error_response_model,
    response_model,
    UpdateAvisoModel,
)
from server.models.view_models import VM_aviso_fecha

router = APIRouter()


@router.get("/", response_description="Avisos retrieved")
async def get_avisos():
    avisos = await retrieve_avisos()
    if avisos:
        return response_model(avisos,
                              "Avisos data retrieved successfully")
    return error_response_model(avisos,
                                404,
                                "Empty list returned")


@router.get("/{id}", response_description="Aviso data retrieved")
async def get_aviso_data(id):
    aviso = await retrieve_aviso(id)
    if aviso:
        return response_model(aviso,
                              "Aviso data retrieved successfully")
    return error_response_model("An error occurred.",
                                404,
                                "Aviso doesn't exist.")


@router.post("/", response_description="Aviso data retrieved")
async def get_aviso_data(vm: VM_aviso_fecha):
    aviso = await retrieve_aviso_between_dates(vm)
    if aviso:
        return response_model(aviso,
                              "Aviso data retrieved successfully")
    return error_response_model("An error occurred.",
                                404,
                                "Aviso doesn't exist.")


@router.put("/{id}")
async def update_aviso_data(id: str, req: UpdateAvisoModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_aviso = await update_aviso(id, req)
    if updated_aviso:
        return response_model(
            "Aviso with ID: {} name update is successful".format(id),
            "Aviso name updated successfully",
        )
    return error_response_model(
        "An error occurred",
        404,
        "There was an error updating the aviso data.",
    )


@router.delete("/{id}", response_description="Aviso data deleted from the database")
async def delete_aviso_data(id: str):
    deleted_aviso = await delete_aviso(id)
    if deleted_aviso:
        return response_model(
            "Aviso with ID: {} removed".format(id),
            "Aviso deleted successfully"
        )
    return error_response_model(
        "An error occurred",
        404,
        "Aviso with id {0} doesn't exist".format(id)
    )
