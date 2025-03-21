import shutil  # Importa el módulo para copiar archivos manteniendo metadatos.
import os  # Importa el módulo para manejar rutas y archivos.

try:
    # Definir la ruta del archivo que se desea copiar
    ruta_documento = r"Ruta de archivo"
    
    # Definir la ruta de la carpeta donde se encuentra el archivo
    ruta_carpeta = r"Carpeta archivo"

    # Verifica si la carpeta especificada existe
    if os.path.isdir(ruta_carpeta):
        # Verifica si el archivo existe en la ruta especificada
        if os.path.exists(ruta_documento):
            # Define la carpeta de destino, en este caso, la carpeta de Descargas del usuario
            ruta_destino = os.path.join(os.path.expanduser("~"), "Downloads")

            # Copia el archivo a la carpeta de destino, manteniendo metadatos (como fecha de modificación)
            shutil.copy2(ruta_documento, ruta_destino)

            # Mensaje de confirmación si la copia fue exitosa
            print(f"Archivo: {ruta_documento} trasladado exitosamente en: {ruta_destino}.")
        else:
            # Mensaje de error si el archivo no se encuentra
            print("Archivo no encontrado.")
    else:
        # Mensaje de error si la carpeta no existe
        print("La carpeta no existe.")

except Exception as error:
    # Captura cualquier error que ocurra en la ejecución del programa
    print(f"Error en el sistema: {error}.")
