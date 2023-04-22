from fastapi import APIRouter, Depends, HTTPException
#from ..controllers.descardar import download_images
from ..controllers.descargar import download_images

router = APIRouter(
    prefix="/api",
    responses={404: {"description": "Not found"}},
)


@router.get("/generar-imagen-alta-calidad")
async def generarImagenAC():

    # llamar a middlewares
    try:
        # llamar a controller
        await download_images()

    except Exception as e:
        print("Un error a ocurrido",e)
        return {
            "estado": 500,
            "mensajeCliente": "error_servidor",
            "resultado": "error servidor"
        }
        
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