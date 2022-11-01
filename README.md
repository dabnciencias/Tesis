# Tesis

En este repositorio comparto los archivos usados para generar [mi tesis de maestría](http://132.248.9.195/ptd2022/septiembre/0831398/Index.html) y [la presentacion de la misma](http://dabnciencias.github.io/Examen_profesional) con el fin de que otras personas que quieran utilizar el mismo formato para sus propios trabajos o quieran tomar resultados de aquí puedan hacerlo con facilidad.

La carpeta `Texto/` contiene los archivos de LaTeX usados para generar la tesis; al ejecutar el archivo principal `tesis.tex` se genera `tesis.pdf`. El archivo `pre.tex` contiene los comandos de configuración del documento, incluyendo ambientes y comandos personalizados, así como paqueterías. Además, se incluyen dos archivos `.pdf` necesarios para generar la portada correctamente.

La carpeta `Presentación/` contiene cuatro subcarpetas:
* `Códigos/`, donde se encuentran los códigos de Python usados para generar las animaciones de la presentación utilizando [Manim](https://www.manim.community/);
* `Diagramas/`, que contiene los archivos `.svg` utilizados en algunas animaciones, así como los archivos `.tex` con los cuales fueron generados;
* `"Una introducción a las categorías extrianguladas"/`, que contiene todas las animaciones de la presentación;
* `media/`, que contiene todas las animaciones generadas por los códigos de `Códigos/` y que son utilizadas para generar la presentación utilizando [Manim Editor](https://docs.editor.manim.community/en/stable/).

Es posible generar la presentación localmente descargando la carpeta `"Una introducción a las categorías extrianguladas"/`, ejecutando en comando `python -m http.server` (suponiendo que Python ya está instalado) desde una terminal virtual ubicada dentro de dicha carpeta, y abriendo un navegador en la página web que indique la terminal después de haber realizado el paso previo.
