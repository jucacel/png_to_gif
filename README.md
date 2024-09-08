# png_to_gif

PNG to GIF Converter
Este script de Python convierte un conjunto de imágenes PNG en una animación GIF. Utiliza las bibliotecas Pillow para la manipulación de imágenes y Tkinter para la selección de directorios y archivos.

Requisitos
Python 3.x
Pillow (pip install Pillow)
Tkinter (normalmente incluido con Python, pero puede necesitar instalación adicional en algunas distribuciones)
Funcionalidad
Selecciona un directorio de entrada: El script permite al usuario seleccionar un directorio que contenga imágenes PNG.
Selecciona un archivo de salida: El usuario elige dónde guardar el archivo GIF resultante.
Convierte las imágenes a GIF: El script toma todas las imágenes PNG en el directorio seleccionado y las convierte en un solo archivo GIF animado.



Uso
Ejecuta el script:

python3 png_to_gif.py

Se abrirá una ventana para que selecciones el directorio que contiene las imágenes PNG.
Luego, se abrirá otra ventana para que elijas el nombre y la ubicación del archivo GIF de salida.
El script convertirá las imágenes y guardará el archivo GIF en la ubicación seleccionada.
Notas
Las imágenes se ordenan alfabéticamente por nombre antes de la conversión.
La duración de cada fotograma en el GIF está configurada en 500 milisegundos (0.5 segundos). Puedes ajustar este valor modificando el parámetro duration en el script.
Contribuciones
Si deseas contribuir al desarrollo del script, por favor realiza un fork del repositorio y envía un pull request con tus cambios.

Licencia
Este proyecto está licenciado bajo los términos de la licencia MIT. Consulta el archivo LICENSE para más detalles.

