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

# Métodos personalizados
def surrounding_box(self, color):
    return Rectangle(stroke_color=color, fill_color=BLACK, width = 13.4, height = self.get_top()[1]-self.get_bottom()[1]+0.5).move_to(self.get_center()).set_x(0)

Mobject.surrounding_box = surrounding_box

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

def update_slide_frame(self, títuloDiapositiva, subtítuloDiapositiva, númeroDiapositiva):
    nuevoTítulo = Tex(títuloDiapositiva).scale(escalaTexto).align_on_border(LEFT+UP, buff = 0.1).match_y(self.camera.frame[2][0])
    nuevoSubtítulo = Tex(subtítuloDiapositiva).scale(escalaTexto).align_on_border(RIGHT+UP, buff = 0.1).match_y(self.camera.frame[2][1])
    nuevoNúmero = Tex(str(númeroDiapositiva)+"/"+númeroTotalDeDiapositivas).scale(escalaPieDePágina).align_on_border(DOWN+RIGHT, buff = 0.1).match_y(self.camera.frame[3][2])
    self.play(Transform(self.camera.frame[2][0],nuevoTítulo),
              Transform(self.camera.frame[2][1],nuevoSubtítulo),
              Transform(self.camera.frame[3][2],nuevoNúmero))

def change_slide_subtitle(self, subtítuloDiapositiva, color=WHITE):
    nuevoSubtítulo = Tex(subtítuloDiapositiva).scale(escalaTexto).align_on_border(RIGHT+UP, buff = 0.1).match_y(self.camera.frame[2][1]).set_color(color)
    return Transform(self.camera.frame[2][1],nuevoSubtítulo)

def change_slide_number(self, númeroDiapositiva):
    nuevoNúmero = Tex(str(númeroDiapositiva)+"/"+númeroTotalDeDiapositivas).scale(escalaPieDePágina).align_on_border(DOWN+RIGHT, buff = 0.1).match_y(self.camera.frame[3][2])
    return Transform(self.camera.frame[3][2],nuevoNúmero)

MovingCameraScene.move_camera = move_camera
MovingCameraScene.add_slide_frame = add_slide_frame
MovingCameraScene.update_slide_frame = update_slide_frame
MovingCameraScene.change_slide_subtitle = change_slide_subtitle
MovingCameraScene.change_slide_number = change_slide_number

class Zcategorias(MovingCameraScene):

    def construct(self):

        # Mobjects
        recordatorio = Tex(r"\flushleft \textbf{Recordatorio} ","Una categoría ", r"$\mathscr{C}$ ", "es una ", r"$\mathbb{Z}$-\emph{categoría} ", r"si \begin{itemize} \item[$\bullet$] $\forall \ A,B\in\mathscr{C}, \ \text{Hom}_\mathscr{C}(A,B)$ tiene estructura de grupo abeliano, y \item[$\bullet$] la composición de morfismos en $\mathscr{C}$ es bilineal.\end{itemize}").scale(escalaTexto).align_on_border(LEFT, buff=buffIzquierdo).shift(2*UP)
        recordatorio[0].set_color(GRIS)
        recordatorio[2].set_color(GRIS)
        recordatorio[4].set_color(GRIS)
        recordatorio[5][8].set_color(GRIS)
        recordatorio[5][13].set_color(GRIS)
        recordatorio[5][78].set_color(GRIS)
        recordatorio = Group(recordatorio.surrounding_box(GRIS), recordatorio)
        obs_1 = Tex(r"\flushleft \textbf{Observación} ", "Si ", r"$\mathscr{C}$ ", "es una ", r"$\mathbb{Z}$-categoría", ", entonces su categoría opuesta ", r"$\mathscr{C}^\text{op}$ ", "también lo es.").scale(escalaTexto).next_to(recordatorio, 2*DOWN).align_on_border(LEFT, buff=buffIzquierdo)
        obs_1[0].set_color(GRIS)
        obs_1[2].set_color(GRIS)
        obs_1[4].set_color(GRIS)
        obs_1[6].set_color(GRIS)
        obs_1 = Group(obs_1.surrounding_box(GRIS), obs_1)
        obs_2 = Tex(r"\flushleft \textbf{Observación} ", "La categoría producto de dos ", r"$\mathbb{Z}$-categorías ", "es una ", r"$\mathbb{Z}$-categoría", ". En particular, si ", r"$\mathscr{C}$ ", "es una ", r"$\mathbb{Z}$-categoría", ", entonces ", r"$\mathscr{C}^\text{op}\times\mathscr{C}$", " también lo es.").scale(escalaTexto).next_to(recordatorio, 2*DOWN).align_on_border(LEFT, buff=buffIzquierdo).shift(1.5*DOWN)
        obs_2[0].set_color(GRIS)
        obs_2[2].set_color(GRIS)
        obs_2[4].set_color(GRIS)
        obs_2[6].set_color(GRIS)
        obs_2[8].set_color(GRIS)
        obs_2[10].set_color(GRIS)
        obs_2 = Group(obs_2.surrounding_box(GRIS), obs_2)

        ejem = Tex(r"\textbf{Ejemplo} ", "La categoría de grupos abelianos Ab es una ", r"$\mathbb{Z}$-categoría", ".").scale(escalaTexto).next_to(obs_2, 2*DOWN).align_on_border(LEFT, buff=buffIzquierdo)
        ejem[0].set_color(GRIS)
        ejem[2].set_color(GRIS)
        ejem = Group(ejem.surrounding_box(GRIS), ejem)

        self.next_section(type=PresentationSectionType.NORMAL)
        self.add_slide_frame("Teoría de bifuntores aditivos", r"$\mathbb{Z}$-categorías", 7)
        self.camera.frame[2][1][:].set_color(GRIS)
        self.add(recordatorio)
        self.move_camera(ORIGIN)

        self.next_section(type=PresentationSectionType.NORMAL)
        self.add(obs_1)
        self.wait()

        self.next_section(type=PresentationSectionType.NORMAL)
        self.add(obs_2)
        self.wait()

        self.next_section(type=PresentationSectionType.NORMAL)
        self.add(ejem)
        self.wait()

class BifuntoresAditivos(MovingCameraScene):

    def construct(self):

        # Mobjects
        rec_1 = Tex(r"\flushleft \textbf{Recordatorio} ","Sean ", r"$\mathscr{C}$ ", "y ", r"$\mathscr{D} \ \mathbb{Z}$-categorías", r". Un funtor (covariante) ", r"$F:\mathscr{C}\to\mathscr{D}$ ", "es ", "\emph{aditivo} ", r"si $F:\text{Hom}_\mathscr{C}(X,Y)\to \text{Hom}_\mathscr{D}(F(X), F(Y))$ es un morfismo de grupos abelianos para cualesquiera $X,Y\in\mathscr{C}$.").scale(escalaTexto).align_on_border(LEFT, buff=buffIzquierdo).shift(2*UP)
        rec_1[0].set_color(GRIS)
        rec_1[2].set_color(GRIS)
        rec_1[4].set_color(GRIS)
        rec_1[6][2].set_color(GRIS)
        rec_1[6][4].set_color(GRIS)
        rec_1[8].set_color(GRIS)
        rec_1[9][7].set_color(GRIS)
        rec_1[9][17].set_color(GRIS)
        rec_1[9][78].set_color(GRIS)
        rec_1 = Group(rec_1.surrounding_box(GRIS), rec_1)
        rec_2 = Tex(r"\flushleft \textbf{Recordatorio} ", r"Un \emph{bifuntor} es un funtor cuyo dominio es una categoría producto de la forma $\mathscr{C}'\times\mathscr{C}$, con $\mathscr{C}$ y $\mathscr{C}'$ categorías.").scale(escalaTexto).next_to(rec_1, 2.25*DOWN).align_on_border(LEFT, buff=buffIzquierdo)
        rec_2[0].set_color(GRIS)
        rec_2 = Group(rec_2.surrounding_box(GRIS), rec_2)
        ejem = Tex(r"\flushleft \textbf{Ejemplo} ", "Si ", r"$\mathscr{C}$ ", "es una ", r"$\mathbb{Z}$-categoría", ", entonces el bifuntor ", r"$$\text{Hom}(-,-):\mathscr{C}^\text{op}\times\mathscr{C}\to\text{Ab}$$ es ", "aditivo", ".").scale(escalaTexto).align_on_border(LEFT, buff=buffIzquierdo).shift(2*DOWN)
        ejem[0].set_color(GRIS)
        ejem[2].set_color(GRIS)
        ejem[4].set_color(GRIS)
        ejem[6][9:14].set_color(GRIS)
        ejem[7].set_color(GRIS)
        ejem = Group(ejem.surrounding_box(GRIS), ejem)

        self.next_section(type=PresentationSectionType.NORMAL)
        self.add_slide_frame("Teoría de bifuntores aditivos", r"Bifuntores aditivos", 8)
        self.add(rec_1)
        self.move_camera(ORIGIN)

        self.next_section(type=PresentationSectionType.NORMAL)
        self.add(rec_2)
        self.wait()

        self.next_section(type=PresentationSectionType.NORMAL)
        self.add(ejem)
        self.wait()

class AccionesAsociadas(MovingCameraScene):

    def construct(self):

        definición = Tex(r"\flushleft \textbf{Definición} ","Sean ", r"$\mathscr{C}$ ", "una ", r"$\mathbb{Z}$-categoría", r", $\mathbb{E}:\mathscr{C}^\text{op}\times\mathscr{C}\to\text{Ab}$ un bifuntor ", r"aditivo y $A,A',C,C'\in\mathscr{C}$", r". Definimos las correspondencias \begin{align*} \text{Hom}_\mathscr{C}(A,A')\times\mathbb{E}(C,A) &\to \mathbb{E}(C,A'), \\ (a,\delta) &\mapsto a\cdot\delta:=\mathbb{E}(C,a)(\delta), \\ \\ \mathbb{E}(C,A)\times\text{Hom}_\mathscr{C}(C',C) &\to \mathbb{E}(C',A), \\ (\delta,c) &\mapsto \delta\cdot c:=\mathbb{E}(c^\text{op},A)(\delta). \end{align*}").scale(escalaTexto).align_on_border(LEFT, buff=buffIzquierdo).shift(UP)
        definición[0].set_color(GRIS)
        definición[2].set_color(GRIS)
        definición[4].set_color(GRIS)
        definición[5][3:8].set_color(GRIS)
        definición[6][0:7].set_color(GRIS)
        definición[6][18].set_color(GRIS)
        definición[7][32].set_color(GRIS)
        definición[7][87].set_color(GRIS)
        definición = Group(definición.surrounding_box(GRIS), definición)

        template = TexTemplate()
        template.add_to_preamble(r"\usepackage[left=1.25in,right=1.25in,top=1in,bottom=1in]{geometry}\usepackage{ragged2e}\usepackage{mathrsfs}")
        prop = Tex(r"\justifying \textbf{Proposición} ","Sean ", r"$\mathscr{C}$ ", "una ", r"$\mathbb{Z}$-categoría ", "y ", r"$\mathbb{E}:\mathscr{C}^\text{op}\times\mathscr{C}\to\text{Ab}$ un bifuntor ", r"aditivo", r". Entonces, las siguientes condiciones se satisfacen. \begin{enumerate} \item[(a)] $a\cdot(\delta_1+\delta_2) = a\cdot\delta_1 + a\cdot\delta_2 \hspace{-0.175mm} \quad \forall \ a\in\text{Hom}_\mathscr{C}(A,A'), \ \delta_1,\delta_2\in\mathbb{E}(C,A)$. \item[(b)] $(a_1+a_1)\cdot\delta = a_1\cdot\delta + a_2\cdot\delta \quad \hspace{-0.845mm} \forall \ a_1,a_2\in\text{Hom}_\mathscr{C}(A,A'), \ \delta\in\mathbb{E}(C,A)$. \item[(c)] $1_A\cdot\delta = \delta \hspace{3.0475cm} \forall \ \delta\in\mathbb{E}(C,A)$. \item[(d)] $(a'a)\cdot\delta = a'\cdot(a\cdot\delta) \hspace{1.45cm} \forall \ a\in\text{Hom}_\mathscr{C}(A,A'), \ a'\in\text{Hom}_\mathscr{C}(A',A''), \ \delta\in\mathbb{E}(C,A)$. \item[(e)] $(\delta_1+\delta_2)\cdot c = \delta_1\cdot c + \delta_2\cdot c \hspace{4.425mm} \forall \ c\in\text{Hom}_\mathscr{C}(C',C), \ \delta_1,\delta_2\in\mathbb{E}(C,A)$. \item[(f)] $\delta\cdot(c_1+c_2)=\delta\cdot c_1 + \delta\cdot c_2 \hspace{4.17mm} \forall \ c_1,c_2\in\text{Hom}_\mathscr{C}(C',C), \ \delta\in\mathbb{E}(C,A)$. \item[(g)] $\delta\cdot1_C  = \delta \hspace{3.055cm} \forall \ \delta\in\mathbb{E}(C,A)$. \item[(h)] $\delta\cdot(cc') = (\delta\cdot c)\cdot c' \hspace{1.6cm} \forall \ c\in\text{Hom}_\mathscr{C}(C',C), \ c'\in\text{Hom}_\mathscr{C}(C'',C'), \ \delta\in\mathbb{E}(C,A)$. \item[(i)] $a\cdot(\delta\cdot c) = (a\cdot\delta)\cdot c \hspace{1.48cm} \forall \ a\in\text{Hom}_\mathscr{C}(A,A'), \ c\in\text{Hom}_\mathscr{C}(C',C), \ \delta\in\mathbb{E}(C,A)$. \item[(j)] $0\cdot\delta = 0 = \delta\cdot0 \hspace{2.22cm} \forall \ \delta\in\mathbb{E}(C,A)$. \end{enumerate}", tex_template=template).scale(0.575).align_on_border(LEFT, buff=buffIzquierdo)#.shift(UP)
        prop[0].set_color(GRIS)
        prop[2].set_color(GRIS)
        prop[4].set_color(GRIS)
        prop[6][2:7].set_color(GRIS)
        prop[7].set_color(GRIS)
        prop[8][75].set_color(GRIS)
        prop[8][128].set_color(GRIS)
        prop[8][189].set_color(GRIS)
        prop[8][203].set_color(GRIS)
        prop[8][250].set_color(GRIS)
        prop[8][303].set_color(GRIS)
        prop[8][364].set_color(GRIS)
        prop[8][378].set_color(GRIS)
        prop[8][421].set_color(GRIS)
        prop[8][434].set_color(GRIS)
        prop = Group(prop.surrounding_box(GRIS), prop)

        self.next_section(type=PresentationSectionType.NORMAL)
        self.add_slide_frame("Teoría de bifuntores aditivos", r"Acciones asociadas", 9)
        self.add(definición)
        self.move_camera(ORIGIN)

        self.next_section(type=PresentationSectionType.NORMAL)
        self.remove(definición)
        prop[1][8][222:].set_fill(opacity=0)
        self.add(prop)
        self.play(self.change_slide_number(10))

        self.next_section(type=PresentationSectionType.NORMAL)
        self.remove(definición)
        prop[1][8][222:397].set_fill(opacity=1)
        self.wait()

        self.next_section(type=PresentationSectionType.NORMAL)
        self.remove(definición)
        prop[1][8][397:].set_fill(opacity=1)
        self.wait()

class CategoriasAditivas(MovingCameraScene):

    def construct(self):

        # Mobjects
        recordatorio = Tex(r"\justifying \textbf{Recordatorio} ","Una categoría ", r"aditiva $\mathscr{A}$ ", "es una ", r"$\mathbb{Z}$-\emph{categoría} ", r"con coproductos finitos, los cuales denotaremos utilizando el símbolo $\bigoplus$.").scale(escalaTexto).align_on_border(LEFT, buff=buffIzquierdo).shift(2.5*UP)
        recordatorio[0].set_color(GRIS)
        recordatorio[2].set_color(GRIS)
        recordatorio[4].set_color(GRIS)
        recordatorio = Group(recordatorio.surrounding_box(GRIS), recordatorio)
        definición = Tex(r"\justifying \textbf{Definición} ", "Sea ", r"$\mathscr{A}$ ", "una categoría ", "aditiva", r". Una \emph{subcategoría} ", r"\emph{aditiva} ", "de ", r"$\mathscr{A}$ ", r"es una subcategoría $\mathscr{A}'$ de $\mathscr{A}$ tal que $\mathscr{A}'$ es una categoría ", "aditiva ", "y todo coproducto finito en $\mathscr{A}'$ es un coproducto finito en $\mathscr{A}$.").scale(escalaTexto).next_to(recordatorio, 2*DOWN).align_on_border(LEFT, buff=buffIzquierdo)
        definición[0].set_color(GRIS)
        definición[2].set_color(GRIS)
        definición[4].set_color(GRIS)
        definición[6].set_color(GRIS)
        definición[8].set_color(GRIS)
        definición[9][21].set_color(GRIS)
        definición[10].set_color(GRIS)
        definición[11][23:25].set_color(GRIS)
        definición[11][47].set_color(GRIS)
        nota = Tex(r"\justifying \textbf{Nota} ", "En todo lo que sigue, ", r"$\mathscr{A}$ ", "representará una ", r"categoría aditiva ", r"y $\mathbb{E}$, un bifuntor ", "aditivo ", "de ", r"$\mathscr{A}^\text{op}\times\mathscr{A}$", " en Ab.").scale(escalaTexto).next_to(definición, 2.75*DOWN).align_on_border(LEFT, buff=buffIzquierdo)
        definición = Group(definición.surrounding_box(GRIS), definición)
        nota[0].set_color(GRIS)
        nota[2].set_color(GRIS)
        nota[4].set_color(GRIS)
        nota[6].set_color(GRIS)
        nota[8].set_color(GRIS)
        nota = Group(nota.surrounding_box(GRIS), nota)

        self.next_section(type=PresentationSectionType.NORMAL)
        self.add_slide_frame("Teoría de bifuntores aditivos", r"Categorías aditivas", 11)
        self.camera.frame[2][1][:].set_color(GRIS)
        self.add(recordatorio)
        self.move_camera(ORIGIN)

        self.next_section(type=PresentationSectionType.NORMAL)
        self.add(definición)
        self.wait()

        self.next_section(type=PresentationSectionType.NORMAL)
        self.add(nota)
        self.wait()
