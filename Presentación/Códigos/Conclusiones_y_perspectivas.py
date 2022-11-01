from manim import *
from manim_editor import PresentationSectionType
from manim.mobject.geometry.tips import ArrowTriangleFilledTip

################################################################
############ Realizado con Manim Community v.0.15.2 ############
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

class Conclusiones(MovingCameraScene):

    def construct(self):

        texto = Tex(r"""\begin{itemize}
                        \item[$\bullet$] Existe una generalización simultánea de las categorías exactas y las categorías trianguladas, dada por las categorías extrianguladas.
                        \item[$\bullet$] Algunas categorías exactas pueden ser vistas como extrianguladas y vice versa. Por otro lado, toda categoría triangulada puede ser vista como extriangulada y algunas extrianguladas pueden ser vistas como trianguladas.
                        \item[$\bullet$] Existen categorías extrianguladas que no son exactas ni trianguladas.
                        \item[$\bullet$] Se pueden definir pares de cotorsión (completos) en este nuevo contexto.
                    \end{itemize}""").scale(escalaTexto).align_on_border(LEFT, buff=buffIzquierdo*1.5)
        texto[0][0].set_color(NARANJA)
        texto[0][49:56].set_color(AMARILLO)
        texto[0][71:83].set_color(ROJO)
        texto[0][104:118].set_color(NARANJA)
        texto[0][119].set_color(NARANJA)
        texto[0][137:144].set_color(AMARILLO)
        texto[0][163:177].set_color(NARANJA)
        texto[0][213:224].set_color(ROJO)
        texto[0][241:255].set_color(NARANJA)
        texto[0][263:277].set_color(NARANJA)
        texto[0][296:308].set_color(ROJO)
        texto[0][309].set_color(NARANJA)
        texto[0][327:341].set_color(NARANJA)
        texto[0][349:356].set_color(AMARILLO)
        texto[0][358:370].set_color(ROJO)
        texto[0][371].set_color(NARANJA)
        texto[0][416:433].set_color(NARANJA)
        texto[0][119:].set_fill(opacity=0)

        self.next_section(type=PresentationSectionType.NORMAL)
        self.add_slide_frame("Conclusiones", "", 25)
        self.add(texto)
        self.move_camera(ORIGIN)

        self.next_section(type=PresentationSectionType.NORMAL)
        texto[0][119:309].set_fill(opacity=1)
        self.wait()

        self.next_section(type=PresentationSectionType.NORMAL)
        texto[0][309:371].set_fill(opacity=1)
        self.wait()

        self.next_section(type=PresentationSectionType.NORMAL)
        texto[0][371:].set_fill(opacity=1)
        self.wait()

class Perspectivas(MovingCameraScene):
    
    def construct(self):

        # Mobjects
        Extrianguladas = Group(Tex("Extrianguladas"), Ellipse(width=4.25, height=1)).set_color(NARANJA).scale(0.9)

        Modelo = Tex(r"Categorías \break modelo \break (e.g. [3])")
        Modelo[0][0:16].set_color(NARANJA)
        Modelo[0][22].set_color(VERDE)
        Modelo = Group(SurroundingRectangle(Modelo, buff=0.25, color=NARANJA), Modelo).next_to(Extrianguladas, 2*UP).scale(0.9)

        Cotorsión = Tex(r"Teoría de \break cotorsión \break (e.g. [4])")
        Cotorsión[0][0:17].set_color(NARANJA)
        Cotorsión[0][23].set_color(VERDE)
        Cotorsión = Group(SurroundingRectangle(Cotorsión, buff=0.25, color=NARANJA), Cotorsión).next_to(Extrianguladas, 5*RIGHT).shift(UP).scale(0.9)

        Superior = Tex(r"Álgebra \break homológica \break ``superior'' \break (e.g. [5])")
        Superior[0][0:29].set_color(NARANJA)
        Superior[0][35].set_color(VERDE)
        Superior = Group(SurroundingRectangle(Superior, buff=0.25, color=NARANJA), Superior).shift(3.25*RIGHT+2.25*DOWN).scale(0.9)

        Relativa = Tex(r"Homología \break relativa \break  (e.g. [6])")
        Relativa[0][0:17].set_color(NARANJA)
        Relativa[0][23].set_color(VERDE)
        Relativa = Group(SurroundingRectangle(Relativa, buff=0.25, color=NARANJA), Relativa).shift(3*LEFT+2*DOWN).scale(0.9)

        Localización = Tex(r"Localización \break (e.g. [7])")
        Localización[0][0:12].set_color(NARANJA)
        Localización[0][18].set_color(VERDE)
        Localización = Group(SurroundingRectangle(Localización, buff=0.25, color=NARANJA), Localización).next_to(Extrianguladas, 5*LEFT).shift(UP).scale(0.9)

        # Primera diapositiva
        self.next_section(type=PresentationSectionType.NORMAL)
        self.add_slide_frame("Perspectivas", "", 26)
        self.add(Extrianguladas)
        self.move_camera(ORIGIN)

        self.next_section(type=PresentationSectionType.NORMAL)
        self.play(GrowFromPoint(Group(Modelo, Line(start=Extrianguladas.get_top(), end=Modelo.get_bottom(), color=NARANJA)), Extrianguladas.get_top()))

        self.next_section(type=PresentationSectionType.NORMAL)
        self.play(GrowFromPoint(Group(Cotorsión, Line(start=[0.9,0.4,0], end=Cotorsión.get_left(), color=NARANJA)), [0.9, 0.4, 0]))

        self.next_section(type=PresentationSectionType.NORMAL)
        self.play(GrowFromPoint(Group(Superior, Line(start=[0.5,-0.45,0], end=Superior.get_left(), color=NARANJA)), [0.5, -0.45, 0]))

        self.next_section(type=PresentationSectionType.NORMAL)
        self.play(GrowFromPoint(Group(Relativa, Line(start=[-0.5,-0.45,0], end=Relativa.get_right(), color=NARANJA)), [-0.5, -0.45, 0]))

        self.next_section(type=PresentationSectionType.NORMAL)
        self.play(GrowFromPoint(Group(Localización, Line(start=[-0.9,0.4,0], end=Localización.get_right(), color=NARANJA)), [-0.9, 0.4, 0]))

        self.next_section(type=PresentationSectionType.NORMAL)
        self.play(FadeIn(DoubleArrow(start=Modelo.get_right(), end=Cotorsión.get_left(), color=NARANJA, buff=0.1)),
                  GrowArrow(Arrow(start=Localización.get_bottom(), end=Superior.get_left(), color=NARANJA, buff=0.1)),
                  GrowArrow(Arrow(start=Cotorsión.get_bottom(), end=Relativa.get_right(), color=NARANJA, buff=0.1))
                  )
        self.wait()
