1. Clona el Repositorio:
------------------------

   Clona el repositorio del proyecto desde GitHub en tu máquina local. Puedes hacerlo ejecutando el siguiente comando en la terminal o línea de comandos:

   git clone https://github.com/alanhenriquez/Compresor_PDF.git


2. Instala Ghostscript:
-----------------------

   • (Predeterminada)   El script depende de Ghostscript para la compresión de archivos PDF. Dentro del 
                        repositorio, encontrarás el ejecutable de Ghostscript para tu sistema operativo 
                        Windows en la carpeta `ghostscript`. Simplemente ejecuta el instalador de Ghostscript 
                        correspondiente a tu sistema operativo Windows.
   • (Opcional)         Tambien puedes optar por descargar el ejecutable que desees desde la pagina oficial: 
                        (Enlace de descarga oficial) - https://ghostscript.com/releases/gsdnld.html
                        En caso de elegir esta opcion, cambia la ruta del archivo "compresor_pdf.py" por la ruta de tu nueva descargar, el cambio se realizará en la linea 91


3. Abre una Terminal o Línea de Comandos:
------------------------------------------

   Abre una terminal o línea de comandos en tu sistema operativo.


4. Navega hasta el Directorio del Repositorio:
-----------------------------------------------

   Utiliza el comando `cd` para navegar hasta el directorio del repositorio clonado.

   cd nombre_del_repositorio


5. Ejecuta el Script:
---------------------

   Una vez dentro del directorio del repositorio, ejecuta el script con el comando `python` o `python3`.

   python compresor_pdf.py


6. Sigue las Instrucciones:
---------------------------

   El script te guiará a través del proceso. Deberás ingresar la ruta del archivo PDF que deseas comprimir, la ruta de salida para el nuevo archivo comprimido (o dejarla en blanco para usar la ruta predeterminada) y el nivel de compresión (de 0 a 4).


7. Opcional: Crea una Copia de Seguridad:
------------------------------------------

   El script te preguntará si deseas crear una copia de seguridad del archivo original antes de sobrescribirlo con el archivo comprimido. Responde "yes" o "no" según tus preferencias.


8. Opcional: Abre el PDF Comprimido:
-------------------------------------

   Finalmente, el script te preguntará si deseas abrir el PDF comprimido. Responde "yes" o "no" según desees abrir el PDF original o el comprimido.





Siguiendo estos pasos, deberías poder utilizar el script para comprimir archivos PDF fácilmente. El repositorio incluye todo lo necesario, incluido el ejecutable de Ghostscript, para que puedas comenzar a usarlo de inmediato. ¡No dudes en personalizar o modificar el script según tus necesidades!

