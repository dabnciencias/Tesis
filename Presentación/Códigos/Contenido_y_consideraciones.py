from manim import *
from manim_editor import PresentationSectionType

################################################################
############ Realizado con Manim Community v.0.14.0 ############
################################################################

# Colores
ROJO = '#FF0000'
AZUL = '#0087FF'
NARANJA = '#FF7700'
VERDE = '#1FFF00'
MAGENTA = '#FF00FF'
AMARILLO = "#FFFF00"
GRIS = "#888888"
MAGENTA_CLARO = "#FF67FF"
AZUL_CLARO = "#9CDCEB"
AZUL_OSCURO = "#1C758A"

# Factores de escala para el texto
escalaTítulo = 0.625
escalaPieDePágina = 0.5
escalaTexto = 0.75
buffTítulo = 0.1
buffPieDePágina = 0.1
buffTexto = 0.025
buffRenglón = 0.05
buffEcuación = 0.1
buffTikz = 0.4
buffRectangle = 0.5
buffIzquierdo= 0.65
buffEnum = 0.25

# Constantes de texto
nombre="Diego Alberto Barceló Nieves"
títuloPresentación="Una introducción a las categorías extrianguladas"
númeroTotalDeDiapositivas = "26"

def move_camera(self, direction, duration=1):
    self.play(self.camera.frame.animate.move_to(direction), run_time=duration)

def add_slide_frame(self, títuloDiapositiva, subtítuloDiapositiva, númeroDiapositiva):

    títulos = Group(
                    Tex(títuloDiapositiva).scale(escalaTexto).align_on_border(LEFT+UP, buff = 0.1),
                    Tex(subtítuloDiapositiva).scale(escalaTexto).align_on_border(RIGHT+UP, buff = 0.1)
                   )
    fondoParaTítulos = SurroundingRectangle(títulos, color=BLACK, fill_opacity=1)

    pies = Group(
                 Tex("Diego Alberto Barceló Nieves").scale(escalaPieDePágina).align_on_border(LEFT+DOWN, buff=0.1),
                 Tex("Una introducción a las categorías extrianguladas").scale(escalaPieDePágina).align_on_border(DOWN, buff=0.1),
                 Tex(str(númeroDiapositiva)+"/"+númeroTotalDeDiapositivas).scale(escalaPieDePágina).align_on_border(DOWN+RIGHT, buff=0.1)
                )
    fondoParaPiesDePágina = SurroundingRectangle(pies, color=BLACK, fill_opacity=1)

    self.camera.frame = Group(fondoParaTítulos, fondoParaPiesDePágina, títulos, pies)

MovingCameraScene.move_camera = move_camera
MovingCameraScene.add_slide_frame = add_slide_frame

class Contenido(MovingCameraScene):

    def construct(self):

        texto = Tex(r"""\begin{itemize}
                        \item[$\bullet$] Introducción
                        \item[$\bullet$] Motivación
                        \item[$\bullet$] Teoría de bifuntores aditivos
                        \item[$\bullet$] Definición de categoría extriangulada
                        \item[$\bullet$] Propiedades fundamentales de categorías extrianguladas
                        \item[$\bullet$] Conclusiones y perspectivas
                    \end{itemize}""").scale(escalaTexto).align_on_border(LEFT, buff=buffIzquierdo*1.5)
        texto[0][13:].set_fill(opacity=0)

        self.next_section(type=PresentationSectionType.NORMAL)
        self.add_slide_frame("Contenido","",1)
        self.add(texto)
        self.move_camera(ORIGIN)

        self.next_section(type=PresentationSectionType.NORMAL)
        texto[0][13:24].set_fill(opacity=1)
        self.wait()

        self.next_section(type=PresentationSectionType.NORMAL)
        texto[0][24:51].set_fill(opacity=1)
        self.wait()

        self.next_section(type=PresentationSectionType.NORMAL)
        texto[0][51:86].set_fill(opacity=1)
        #self.wait() #Aquí hay un glitch

        self.next_section(type=PresentationSectionType.NORMAL)
        texto[0][51:86].set_fill(opacity=1)
        self.wait()

        self.next_section(type=PresentationSectionType.NORMAL)
        texto[0][86:137].set_fill(opacity=1)
        self.wait()

        self.next_section(type=PresentationSectionType.NORMAL)
        texto[0][137:].set_fill(opacity=1)
        self.wait()

class Consideraciones(MovingCameraScene):

    def construct(self):

        texto = Tex(r"""
                        \begin{itemize}
                        \item[$\bullet$] Todas las categorías abelianas lo son en el sentido de Mitchell.
                        \item[$\bullet$] Todas las categorías exactas lo son en el sentido de Quillen.
                    \end{itemize}""").scale(escalaTexto).align_on_border(LEFT, buff=buffIzquierdo)
        texto[0][0:15].align_on_border(LEFT, buff=buffIzquierdo)
        texto[0][0].set_color(AZUL)
        texto[0][19:28].set_color(AZUL)
        texto[0][46:54].set_color(AZUL)
        texto[0][55].set_color(AMARILLO)
        texto[0][74:81].set_color(AMARILLO)
        texto[0][99:106].set_color(AMARILLO)
        texto[0][55:].set_fill(opacity=0)

        self.next_section(type=PresentationSectionType.NORMAL)
        self.add_slide_frame("Consideraciones", "", 2)
        self.add(texto)
        self.move_camera(ORIGIN)

        self.next_section(type=PresentationSectionType.NORMAL)
        texto[0][55:].set_fill(opacity=1)
        self.wait()
