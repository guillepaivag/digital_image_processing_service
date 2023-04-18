from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(
    prefix="/api",
    responses={404: {"description": "Not found"}},
)


@router.post("/generar-imagen-alta-calidad")
async def generarImagenAC():

    # llamar a middlewares

    # llamar a controller

    return {
        "estado": 200,
        "mensajeCliente": "exito",
        "resultado": "exito"
    }


@router.post("/generar-dicom-alta-calidad")
async def generarDicomAC():

    # llamar a middlewares

    # llamar a controller

    return {
        "estado": 200,
        "mensajeCliente": "exito",
        "resultado": "exito"
    }


@router.post("/generar-dicom-baja-calidad")
async def generarDicomBC():

    # llamar a middlewares

    # llamar a controller

    return {
        "estado": 200,
        "mensajeCliente": "exito",
        "resultado": "exito"
    }