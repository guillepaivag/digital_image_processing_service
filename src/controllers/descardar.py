import os
import urllib.request
from firebase_admin import storage


def download_images(id_escaneo: str):
    bucket = storage.bucket()
    blob_list = list(bucket.list_blobs(prefix=f'escaneos/{id_escaneo}'))

    for blob in blob_list:
        # Obtener el nombre del archivo
        filename = os.path.basename(blob.name)

        # Descargar la imagen
        url = blob.generate_signed_url(expiration=600)  # 10 minutos
        urllib.request.urlretrieve(url, f'{id_escaneo}/{filename}')