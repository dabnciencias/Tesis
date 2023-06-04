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
escalaTexto = 0.75
buffTítulo = 0.1

# Métodos personalizados
def move_camera(self, direction, duration=1):
    self.play(self.camera.frame.animate.move_to(direction), run_time=duration)

MovingCameraScene.move_camera = move_camera

class Portada(MovingCameraScene):
    def construct(self):
        logoUNAM = SVGMobject("../../LaTeX/logo_UNAM.svg").set_color(BLACK).scale(1.5).align_on_border(UP+LEFT, buff=0.4)
        logoIMATE = SVGMobject("../../LaTeX/logo_IMATE.svg").scale(1.25).align_on_border(UP+RIGHT, buff=0.25).shift(0.35*DOWN)
        título1 = Tex(r"Una introducción a las categorías").set_color(BLACK).set_x(0).scale(1.5).shift(0.2*DOWN)
        título2 = Tex(r"extrianguladas").set_color(BLACK).next_to(título1, DOWN).set_x(0).scale(1.5)
        nombre = Tex("Diego Alberto Barceló Nieves").scale(0.9).set_color(BLACK).next_to(título2, 1.25*DOWN).set_x(0)
        lugar = Tex("Instituto de Matemáticas, UNAM").set_color(BLACK).next_to(nombre, 1.25*DOWN).set_x(0).scale(0.75)
        director = Tex("Director de tesis: Dr. Octavio Mendoza Hernández").set_color(BLACK).next_to(lugar, 0.5*DOWN).set_x(0).scale(0.75)
        fecha = Tex("octubre de 2022").set_color(BLACK).next_to(director, 0.5*DOWN).set_x(0).scale(0.75)
        portada = Group (logoUNAM, logoIMATE, título1, título2, nombre, lugar, director, fecha)

        self.next_section(type=PresentationSectionType.NORMAL)
        self.camera.background_color = WHITE
        self.add(portada)
        self.wait()

class Introduccion(MovingCameraScene):
    def construct(self):
        título = Tex(r"\textbf{Introducción}").scale(1.5).set_x(0)
        self.next_section(type=PresentationSectionType.NORMAL)
        self.add(título)
        self.wait()

class Motivacion(MovingCameraScene):
    def construct(self):
        título = Tex(r"\textbf{Motivación}").scale(1.5).set_x(0)
        self.next_section(type=PresentationSectionType.NORMAL)
        self.add(título)
        self.wait()

class TeoriaDeBifuntoresAditivos(MovingCameraScene):
    def construct(self):
        título1 = Tex(r"\textbf{Teoría de bifuntores}").scale(1.5).set_x(0)
        título2 = Tex(r"\textbf{aditivos}").scale(1.5).next_to(título1, DOWN)
        título = Group(título1, título2).set_y(0)
        self.next_section(type=PresentationSectionType.NORMAL)
        self.add(título)
        self.wait()

class DefinicionCategoriaExtriangulada(MovingCameraScene):
    def construct(self):
        título1 = Tex(r"\textbf{Definición de categoría}").scale(1.5).set_x(0)
        título2 = Tex(r"\textbf{extriangulada}").scale(1.5).next_to(título1, DOWN)
        título = Group(título1, título2).set_y(0)
        self.next_section(type=PresentationSectionType.NORMAL)
        self.add(título)
        self.wait()

class PropiedadesFundamentales(MovingCameraScene):
    def construct(self):
        título1 = Tex(r"\textbf{Propiedades fundamentales de}").scale(1.5).set_x(0)
        título2 = Tex(r"\textbf{categorías extrianguladas}").scale(1.5).next_to(título1, DOWN)
        título = Group(título1, título2).set_y(0)
        self.next_section(type=PresentationSectionType.NORMAL)
        self.add(título)
        self.wait()

class ConclusionesPerspectivas(MovingCameraScene):
    def construct(self):
        título1 = Tex(r"\textbf{Conclusiones y}").scale(1.5).set_x(0)
        título2 = Tex(r"\textbf{perspectivas}").scale(1.5).next_to(título1, DOWN)
        título = Group(título1, título2).set_y(0)
        self.next_section(type=PresentationSectionType.NORMAL)
        self.add(título)
        self.wait()

class Referencias(MovingCameraScene):
    def construct(self):
        título = Tex("Referencias").scale(escalaTítulo).align_on_border(LEFT+UP, buff=buffTítulo)
        ref1 = Tex(r"\flushleft [1] L. Salce. ``Cotorsion Theories for Abelian Groups''. En: \emph{Symp. Math.} (1979), págs. 11-32.").scale(0.8).shift(2*UP).align_on_border(LEFT, buff=0.25)
        ref1[0][1].set_color(VERDE)
        ref2 = Tex(r"\flushleft [2] E. B. Arentz-Hansen. ``Classifying Subcategories in Quotients of Exact Categories''. Tesis de maestría. Norwegian University of Science and Technology, dic. de 2017.").next_to(ref1, 3.25*DOWN).scale(0.8).align_on_border(LEFT, buff=0.25)
        ref2[0][1].set_color(VERDE)
        ref3 = Tex(r"\flushleft [3] H. Nakaoka e Y. Palu. ``Extriangulated Categories, Hovey Twin Cotorsion Pairs and Model Structures''. En: \emph{Cah. Top. Géom. Différ. Catég.} 60.2 (2019), págs. 117-193.").next_to(ref2, 3.25*DOWN).scale(0.8).align_on_border(LEFT, buff=0.25)
        ref3[0][1].set_color(VERDE)
        ref4 = Tex(r"\flushleft [4] M. Huerta, O. Mendoza, C. Sáenz y V. Santiago. ``Cut Notions in Extriangulated Categories Related to Auslander-Buchweitz Theory and Cotorsion Theory''. (2022) DOI: 10.48550/arXiv.2209.08658.").next_to(ref3, 3.25*DOWN).scale(0.8).align_on_border(LEFT, buff=0.25)
        ref4[0][1].set_color(VERDE)
        ref5 = Tex(r"\flushleft [5] M. Herschend, Y. Liu y H. Nakaoka. ``n-exangulated Categories (I): Definitions and Fundamental Properties''. En: \emph{J. Algebra} 570 (2021), págs. 531-586.").next_to(ref4, 3.25*DOWN).scale(0.8).align_on_border(LEFT, buff=0.25)
        ref5[0][1].set_color(VERDE)
        ref6 = Tex(r"\flushleft [6] Y. Ma, Y. Zhang y N. Ding. ``Auslander-Buchweitz Approximation Theory for Extriangulated Categories''. (2020) DOI: 10.48550/arXiv.2006.05112.").next_to(ref5, 3.25*DOWN).scale(0.8).align_on_border(LEFT, buff=0.25)
        ref6[0][1].set_color(VERDE)
        ref7 = Tex(r"\flushleft [7] H. Nakaoka, Y. Ogawa y A. Sakai. ``Localization of Extriangulated Categories''. En: \emph{J. Algebra} 611 (2022), págs. 341-398.").next_to(ref6, 3.25*DOWN).scale(0.8).align_on_border(LEFT, buff=0.25)
        ref7[0][1].set_color(VERDE)

        textos = Group(título, ref1, ref2, ref3, ref4, ref5, ref6, ref7)

        self.next_section(type=PresentationSectionType.NORMAL)
        self.add(textos)
        self.wait()

        self.next_section(type=PresentationSectionType.NORMAL)
        self.move_camera(7.75*DOWN)
        self.wait()
