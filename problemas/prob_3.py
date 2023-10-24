import os
import requests
import zipfile
from io import BytesIO


url = 'https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?auto=format&fit=crop&q=60&w=500&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8cGVycml0b3xlbnwwfHwwfHx8MA%3D%3D'


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
}

response = requests.get(url, headers=headers)

# Verificamos si la descarga fue exitosa
if response.status_code == 200:

    zip_buffer = BytesIO()
    
    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED, False) as zipf:
        # Guardamos la imagen descargada en el archivo ZIP
        zipf.writestr("imag_perrito.jpg", response.content)
    
    # Guardamos el archivo ZIP en el disco
    with open("imagenes.zip", "wb") as zip_file:
        zip_file.write(zip_buffer.getvalue())

    print("La imagen se almacenó satisfactoriamente")
    
    # Ahora descomprimimos el archivo zip
    with zipfile.ZipFile("imagenes.zip", 'r') as zipf:
        zipf.extractall("dir_unzip")

else:
    print("No se pudo descargar la imagen.")


if os.path.exists("dir_unzip"):
    os.chdir("dir_unzip")

