# Traspasador de Archivos

## Descripción
Este proyecto permite copiar archivos desde una ubicación específica en el sistema a la carpeta de descargas del usuario de manera automatizada.  

## Características
- Verifica si la carpeta de origen existe.  
- Comprueba si el archivo está disponible antes de copiarlo.  
- Mantiene los metadatos del archivo original al copiarlo.  
- Maneja errores para evitar interrupciones inesperadas.  

## Requisitos
- Python 3.x  
- Módulos integrados: `shutil`, `os`  

## Uso
1. Define la ruta del archivo a copiar.  
2. Define la carpeta de destino (por defecto, la carpeta de descargas del usuario).  
3. Ejecuta el script y el archivo se trasladará automáticamente.  

## Advertencia
Asegúrate de no compartir rutas locales sensibles si subes este proyecto a un repositorio público.  

## Autor
Camilo Muñoz  
