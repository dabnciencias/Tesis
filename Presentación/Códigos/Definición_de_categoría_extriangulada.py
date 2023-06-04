from manim import *
from manim_editor import PresentationSectionType
from manim.mobject.geometry import ArrowTriangleFilledTip #Es necesario agregar ".tips" a "manim.object.geometry" para algunas versiones de manim más recientes que v.0.14.0

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

# Comandos de LaTeX personalizados y paquetes TODO: Configurar el tex_template de un jalón para no tener que especificarlo muchas veces
myTemplate = TexTemplate(preamble=r"""
                                      \usepackage[spanish]{babel}
                                      \usepackage{amsmath}
                                      \usepackage{amssymb}
                         """)
myTemplate.add_to_preamble(r"""
                               \usepackage{ragged2e}
                               \usepackage{mathrsfs}
                               \makeatletter
                               \newcommand*{\da@xarrow}[7]{%
                                 % #1: below
                                 % #2: above
                                 % #3: arrow left
                                 % #4: arrow right
                                 % #5: space left 
                                 % #6: space right
                                 % #7: math style 
                                 \sbox0{$\ifx#7\scriptstyle\scriptscriptstyle\else\scriptstyle\fi#5#1#6\m@th$}%
                                 \sbox2{$\ifx#7\scriptstyle\scriptscriptstyle\else\scriptstyle\fi#5#2#6\m@th$}%
                                 \sbox4{$#7\dabar@\m@th$}%
                                 \dimen@=\wd0 %
                                 \ifdim\wd2 >\dimen@
                                   \dimen@=\wd2 %   
                                 \fi
                                 \count@=2 %
                                 \def\da@bars{\dabar@\dabar@}%
                                 \@whiledim\count@\wd4<\dimen@\do{%
                                   \advance\count@\@ne
                                   \expandafter\def\expandafter\da@bars\expandafter{%
                                     \da@bars
                                     \dabar@ 
                                   }%
                                 }%  
                                 \mathrel{#3}%
                                 \mathrel{%   
                                   \mathop{\da@bars}\limits
                                   \ifx\\#1\\%
                                   \else
                                     _{\copy0}%
                                   \fi
                                   \ifx\\#2\\%
                                   \else
                                     ^{\copy2}%
                                   \fi
                                 }%   
                                 \mathrel{#4}%
                               }
                               \newcommand*{\da@rightarrow}{\mathchar"0\hexnumber@\symAMSa 4B }
                               \newcommand*{\da@leftarrow}{\mathchar"0\hexnumber@\symAMSa 4C }
                               \newcommand*{\xdashrightarrow}[2][]{%
                                 \mathrel{%
                                   \mathpalette{\da@xarrow{#1}{#2}{}\da@rightarrow{\,}{}}{}%
                                 }%
                               }
                               \makeatother
                           """)

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

def change_slide_subtitle(self, subtítuloDiapositiva):
    nuevoSubtítulo = Tex(subtítuloDiapositiva).scale(escalaTexto).align_on_border(RIGHT+UP, buff = 0.1).match_y(self.camera.frame[2][1])
    return Transform(self.camera.frame[2][1],nuevoSubtítulo)

MovingCameraScene.move_camera = move_camera
MovingCameraScene.add_slide_frame = add_slide_frame
MovingCameraScene.update_slide_frame = update_slide_frame
MovingCameraScene.change_slide_subtitle = change_slide_subtitle

# Mobjects personalizados
class DashedArrow(DashedLine):
    
    def __init__(
        self,
        *args,
        stroke_width=6,
        buff=MED_SMALL_BUFF,
        max_tip_length_to_length_ratio=0.25,
        max_stroke_width_to_length_ratio=5,
        **kwargs,
    ):
        self.max_tip_length_to_length_ratio = max_tip_length_to_length_ratio
        self.max_stroke_width_to_length_ratio = max_stroke_width_to_length_ratio
        tip_shape = kwargs.pop("tip_shape", ArrowTriangleFilledTip)
        super().__init__(*args, buff=buff, stroke_width=stroke_width, **kwargs)
        # TODO, should this be affected when
        # Arrow.set_stroke is called?
        self.initial_stroke_width = self.stroke_width
        self.add_tip(tip_shape=tip_shape)
        self._set_stroke_width_from_length()

    def scale(self, factor, scale_tips=False, **kwargs):

        if self.get_length() == 0:
            return self

        if scale_tips:
            super().scale(factor, **kwargs)
            self._set_stroke_width_from_length()
            return self

        has_tip = self.has_tip()
        has_start_tip = self.has_start_tip()
        if has_tip or has_start_tip:
            old_tips = self.pop_tips()

        super().scale(factor, **kwargs)
        self._set_stroke_width_from_length()

        if has_tip:
            self.add_tip(tip=old_tips[0])
        if has_start_tip:
            self.add_tip(tip=old_tips[1], at_start=True)
        return self


    def get_normal_vector(self) -> np.ndarray:
        
        p0, p1, p2 = self.tip.get_start_anchors()[:3]
        return normalize(np.cross(p2 - p1, p1 - p0))


    def reset_normal_vector(self):

        self.normal_vector = self.get_normal_vector()
        return self


    def get_default_tip_length(self) -> float:

        max_ratio = self.max_tip_length_to_length_ratio
        return min(self.tip_length, max_ratio * self.get_length())


    def _set_stroke_width_from_length(self):

        max_ratio = self.max_stroke_width_to_length_ratio
        if config.renderer == "opengl":
            self.set_stroke(
                width=min(self.initial_stroke_width, max_ratio * self.get_length()),
                recurse=False,
            )
        else:
            self.set_stroke(
                width=min(self.initial_stroke_width, max_ratio * self.get_length()),
                family=False,
            )
        return self

class Idea(MovingCameraScene):

    def construct(self):
        template = TexTemplate()
        template.add_to_preamble(r"\usepackage[left=3in,right=3in,top=1in,bottom=1in]{geometry}")
        texto = Tex(r"Idea: \emph{El bifuntor} $\text{Ext}^1$ \emph{tiene propiedades ``lo suficientemente interesantes'' como para querer interpretar a cualquier bifuntor aditivo a través de ellas.", tex_template=template).scale(1.5)
        texto[0][0:5].set_color(NARANJA)

        # Animación de la escena

        # Primera diapositiva
        self.next_section(type=PresentationSectionType.NORMAL)
        self.add(texto)
        self.wait()

class Eextensiones(MovingCameraScene):

    def construct(self):

        # Mobjects
        texto1 = Tex(r"\justifying \textbf{Definición} Para cualesquiera $A,C\in\mathscr{A}$, una $\mathbb{E}$-\emph{extensión} es un elemento $\delta\in\mathbb{E}(C,A)$. Por ende, formalmente, una $\mathbb{E}$-extensión es una terna $(A,\delta,C)$. En particular, decimos que el elemento $0\in\mathbb{E}(C,A)$ es la $\mathbb{E}$-\emph{extensión escindible}.").scale(escalaTexto).to_edge(LEFT, buff=buffTítulo+0.1).shift(2*UP).set_x(0)
        texto1[0][0:10].set_color(NARANJA)
        texto1[0][30].set_color(GRIS)
        recuadro1 = texto1.surrounding_box(NARANJA)

        texto2 = Tex(r"\justifying \textbf{Definición} Sean $(A,\delta,C)$ y $(A',\delta',C')$ $\mathbb{E}$-extensiones. Un par de morfismos $a\in\text{Hom}_\mathscr{A}(A,A')$ y $c\in\text{Hom}_\mathscr{A}(C,C')$ es un \emph{morfismo de} $\mathbb{E}$-\emph{extensiones} si $a\cdot\delta = \delta'\cdot c$, y lo denotamos por $(a,c):\delta\to\delta'$.").scale(escalaTexto).to_edge(LEFT, buff=buffTítulo+0.1).set_x(0)
        texto2[0][0:10].set_color(NARANJA)
        texto2[0][67].set_color(GRIS)
        texto2[0][80].set_color(GRIS)
        recuadro2 = texto2.surrounding_box(NARANJA)

        recuadros = Group(recuadro1, texto1, recuadro2, texto2)
        recuadros[2].set_stroke(opacity=0)
        recuadros[3].set_fill(opacity=0)

        # Animación de la escena

        # Primera diapositiva
        self.next_section(type=PresentationSectionType.NORMAL)
        self.add(recuadros)
        self.add_slide_frame("Definición de categoría extriangulada", "$\\mathbb{E}$-extensiones", 12)
        self.move_camera(ORIGIN)

        self.next_section(type=PresentationSectionType.NORMAL)
        recuadros[2].set_stroke(opacity=1)
        recuadros[3].set_fill(opacity=1)
        self.wait()

class RelacionDeEquivalencia(MovingCameraScene):

    def construct(self):

        texto1 = Tex(r"\flushleft \textbf{Definición} Sean $A,C\in\mathscr{A}$. Dos sucesiones de morfismos $A\xrightarrow{x}B\xrightarrow{y}C$ y $A\xrightarrow{x'}B'\xrightarrow{y'}C$ en $\mathscr{A}$ son \emph{equivalentes} si existe un isomorfismo $b\in\text{Hom}_\mathscr{A}(B,B')$ tal que el siguiente diagrama conmuta \break \vspace{5mm}", "Esto es una relación de equivalencia; denotamos las clases de equivalencia con corchetes ($[ \ ]$).").scale(escalaTexto).to_edge(LEFT, buff=buffTítulo+0.1).shift(1.5*UP).set_x(0)
        texto1[0][0:10].set_color(NARANJA)
        texto1[0][18].set_color(GRIS)
        texto1[0][68].set_color(GRIS)
        texto1[0][110].set_color(GRIS)
        texto1[0][105:].shift(0.15*DOWN)
        texto1[1][67:].shift(0.35*UP)
        texto1[1].shift(3.75*DOWN)
        texto1[1].set_fill(opacity=0)

        ecuación1 = SVGMobject("../Diagramas/Relación_de_equivalencia.svg").set_color(WHITE).shift(0.5*DOWN)
        eq1 = MathTex("(1)")
        eq1[0][1].set_color(NARANJA)
        eq1.move_to(ecuación1.get_center()).to_edge(RIGHT, buff=1.5*buffIzquierdo)

        texto2 = Tex(r"Para cualesquiera $A,C\in\mathscr{A}$, denotamos ", r"$$0:= \bigg[ A \xrightarrow{\big(\begin{smallmatrix}1 \\ 0\end{smallmatrix}\big)} A\bigoplus C \xrightarrow{(\begin{smallmatrix} 0 &1 \end{smallmatrix})} C \bigg].$$").scale(escalaTexto).next_to(texto1,DOWN)
        texto2[0].to_edge(LEFT, buff=buffIzquierdo)
        texto2[0][20].set_color(GRIS)
        texto2[1].set_x(0)

        texto3 = Tex(r"Para cualesquiera dos clases de equivalencia de sucesiones de morfismos ", r"$[A\xrightarrow{x}B\xrightarrow{y}C]$ y $[A'\xrightarrow{x'}B'\xrightarrow{y'}C']$, denotamos ", r"$$[A\xrightarrow{x}B\xrightarrow{y}C]\bigoplus[A'\xrightarrow{x'}B'\xrightarrow{y'}C'] := \bigg[A\bigoplus A' \xrightarrow{x\bigoplus x'} B\bigoplus B' \xrightarrow{y\bigoplus y'} C\bigoplus C'\bigg].$$").scale(escalaTexto).next_to(texto2,1.5*DOWN).set_x(0)
        texto3[0].to_edge(LEFT, buff=buffIzquierdo)
        texto3[1].to_edge(LEFT, buff=buffIzquierdo)
        texto3[2].to_edge(LEFT, buff=buffIzquierdo)
        texto3[2].scale(0.9).set_x(0)

        textos = Group(texto1, texto2, texto3)
        recuadro = textos.surrounding_box(NARANJA)

        # Animación de la escena

        # Primera diapositiva
        self.next_section(type=PresentationSectionType.NORMAL)
        self.add(recuadro, texto1, ecuación1, eq1, texto2)
        self.add_slide_frame("Definición de categoría extriangulada", "Relación de equivalencia", 13)
        self.move_camera(ORIGIN)

        self.next_section(type=PresentationSectionType.NORMAL)
        texto1[1].set_fill(opacity=1)
        self.wait()

        self.next_section(type=PresentationSectionType.NORMAL)
        self.move_camera(6.8*DOWN)
        self.wait()

        self.next_section(type=PresentationSectionType.NORMAL)
        self.add(texto3)
        self.wait()

class RealizacionAditiva(MovingCameraScene):

    def construct(self):

        # Mobjects
        texto1 = Tex(r"\justifying \textbf{Definición} Una \emph{realización} de $\mathbb{E}$ es una correspondencia $\mathfrak{s}$ que asocia a cada $\mathbb{E}$-extensión $\delta\in\mathbb{E}(C,A)$ una clase de equivalencia $\mathfrak{s}(\delta) = [A\xrightarrow{x} B\xrightarrow{y} C]$ tal que se cumple la siguiente condición.").scale(escalaTexto).to_edge(LEFT, buff=buffTítulo+0.1).shift(2.25*UP).set_x(0)
        texto1[0][0:10].set_color(NARANJA)

        template = TexTemplate()
        template.add_to_preamble(r"\usepackage[left=2in,right=2in,top=1in,bottom=1in]{geometry}\usepackage{ragged2e}\usepackage{mathrsfs}")
        texto2 = Tex(r"\justifying $(\ast)$ Sean $\delta\in\mathbb{E}(C,A)$ y $\delta'\in\mathbb{E}(C',A')$, con $\mathfrak{s}(\delta) = $", r"$[A\xrightarrow{x} B\xrightarrow{y} C]$ y $\mathfrak{s}(\delta') = [A'\xrightarrow{x'} B'\xrightarrow{y'} C']$. Entonces, para cualquier morfismo de $\mathbb{E}$-extensiones ", r"$(a,c):\delta\to\delta'$, existe un morfismo $b\in\text{Hom}_\mathscr{A}(B,B')$ que hace conmutar el ", "siguiente diagrama", tex_template=template).next_to(texto1,DOWN, buff=buffRenglón).scale(escalaTexto).to_edge(LEFT).set_x(0)
        texto2[0][1].set_color(NARANJA)
        texto2[2][31].set_color(GRIS)
        texto2[2].shift(0.1*DOWN)
        texto2[3].shift(0.2*DOWN)

        ecuación1 = SVGMobject("../Diagramas/Realizaciones.svg").set_color(WHITE).next_to(texto2,DOWN,buff=0).scale(escalaTexto).set_x(0)
        ref = MathTex("(2)").scale(escalaTexto).next_to(ecuación1,RIGHT).to_edge(RIGHT, buff=0.75)
        ref[0][1].set_color(NARANJA)
        ecuación1 = Group(ecuación1, ref)

        texto3 = Tex(r"En este caso, decimos que $A\xrightarrow{x} B\xrightarrow{y} C$ \emph{realiza} a $\delta$ y que $(a,b,c)$ \emph{realiza} a $(a,c)$.").next_to(ecuación1,DOWN, buff=2*buffEcuación).scale(escalaTexto).to_edge(LEFT).set_x(0)

        texto4 = Tex(r"Una realización $\mathfrak{s}$ es \emph{aditiva} si cumple las siguientes condiciones.").next_to(texto3,DOWN, buff=buffTikz).scale(escalaTexto).to_edge(LEFT, buff=buffIzquierdo)
        texto4[0][14].set_color(NARANJA)

        texto5 = Tex(r"(i) Para cualesquiera $A,C\in\mathscr{A}$, $0\in\mathbb{E}(C,A)$ satisface $\mathfrak{s}(0)=0$.").next_to(texto4, DOWN, buff=buffEnum).scale(escalaTexto).to_edge(LEFT, buff=buffIzquierdo+0.2)
        texto5[0][23].set_color(GRIS)
        texto5[0][42].set_color(NARANJA)

        texto6 = Tex(r"(ii) Para cualesquiera $\mathbb{E}$-extensiones $\delta\in\mathbb{E}(C,A), \ \delta'\in\mathbb{E}(C',A')$ se tiene que").next_to(texto5,DOWN, buff=buffEnum).scale(escalaTexto).to_edge(LEFT, buff=buffIzquierdo+0.2)
        texto6[:].set_fill(opacity=0)

        ecuación2 = MathTex(r"\mathfrak{s}\big(\delta\bigoplus\delta'\big) = \mathfrak{s}(\delta)\bigoplus\mathfrak{s}(\delta').").scale(escalaTexto).next_to(texto6,DOWN,buff=buffEnum).set_x(0)
        ecuación2[0][0].set_color(NARANJA)
        ecuación2[0][8].set_color(NARANJA)
        ecuación2[0][13].set_color(NARANJA)
        ecuación2[:].set_fill(opacity=0)

        textos = Group(texto1,texto2,ecuación1,texto3,texto4,texto5,texto6,ecuación2)
        textos.set_x(0)
        textos[3].set_fill(opacity=0)
        recuadro1 = textos.surrounding_box(NARANJA)

        texto7 = Tex(r"\justifying \textbf{Nota} En todo lo que sigue, $\mathfrak{s}$ denotará una realización aditiva.").next_to(ecuación2, DOWN, buff=0.75).scale(escalaTexto).to_edge(LEFT, buff=buffIzquierdo)
        texto7[0][0:4].set_color(NARANJA)
        texto7[0][21].set_color(NARANJA)
        texto7[0][33:51].set_color(NARANJA)
        recuadro2 = texto7.surrounding_box(NARANJA)
        texto7.set_fill(opacity=0)
        recuadro2.set_stroke(opacity=0)

        # Animación de la escena

        # Primera diapositiva
        self.next_section(type=PresentationSectionType.NORMAL)
        self.add_slide_frame("Definición de categoría extriangulada", "Realización aditiva", 14)
        self.add(recuadro1, textos, recuadro2, texto7)
        self.move_camera(ORIGIN)

        self.next_section(type=PresentationSectionType.NORMAL)
        textos[3].set_fill(opacity=1)
        self.wait()
        
        self.next_section(type=PresentationSectionType.NORMAL)
        self.move_camera(7*DOWN)
        self.wait()

        self.next_section(type=PresentationSectionType.NORMAL)
        texto6[:].set_fill(opacity=1)
        ecuación2[:].set_fill(opacity=1)
        self.wait()

        self.next_section(type=PresentationSectionType.NORMAL)
        texto7.set_fill(opacity=1)
        recuadro2.set_stroke(opacity=1)
        self.wait()

class Visualizacion(MovingCameraScene):

    def construct(self):

        # Mobjects
        puntoGris = Dot()
        puntoGrisPunteado = Group(puntoGris, Tex(r"\dots").next_to(puntoGris,RIGHT), Tex(r"\vdots").next_to(puntoGris,UP))
        puntos = Group(puntoGrisPunteado, puntoGrisPunteado.copy().rotate_about_origin(PI/2).shift(0.75*LEFT), puntoGrisPunteado.copy().rotate_about_origin(PI).shift(0.75*(LEFT+DOWN)), puntoGrisPunteado.copy().rotate_about_origin(3*PI/2).shift(0.75*DOWN)).shift(4.5*LEFT)
        dominio = Group(MathTex(r"\mathscr{A}^\text{op}\times\mathscr{A}").scale(escalaTexto).next_to(puntos, 2*UP), puntos).set_color(GRIS)

        círculoBlanco = Circle(radius=0.3)
        círculoBlancoPunteado = Group(círculoBlanco, Tex(r"\dots").next_to(círculoBlanco,RIGHT), Tex(r"\vdots").next_to(círculoBlanco,UP))
        círculos = Group(círculoBlancoPunteado, círculoBlancoPunteado.copy().rotate_about_origin(PI/2).shift(0.75*LEFT), círculoBlancoPunteado.copy().rotate_about_origin(PI).shift(0.75*(LEFT+DOWN)), círculoBlancoPunteado.copy().rotate_about_origin(3*PI/2).shift(0.75*DOWN))
        bifuntorAditivo = Group(MathTex(r"\mathbb{E}").scale(escalaTexto).next_to(círculos, 3.5*LEFT).shift(0.75*UP+0.06*RIGHT), Arrow(path_arc=-1.5).next_to(círculos, 0.5*LEFT).shift(0.25*UP), círculos).set_color(WHITE)

        delta = MathTex(r"\delta").set_color(WHITE).move_to(círculoBlanco.get_center()).scale(0.5)
        deltaPrima = MathTex(r"\delta'").set_color(WHITE).move_to(círculoBlanco.get_center()).shift(0.75*DOWN).scale(0.5)

        círculoNaranja = Circle(radius=1.2).shift(4.5*RIGHT+0.4*DOWN).set_color(NARANJA)
        realizaciónAditiva = Group(MathTex(r"\mathfrak{s}").scale(escalaTexto).next_to(círculos, 4*RIGHT).shift(0.7*UP+0.05*RIGHT), Arrow(path_arc=-1.5).next_to(círculos, 0.5*RIGHT).shift(0.25*(UP+RIGHT))).set_color(NARANJA)

        realizaciónDelta = MathTex(r"[A\xrightarrow{x} B\xrightarrow{y} C]").scale(0.5).set_color(NARANJA).move_to(círculoNaranja.get_center()).shift(0.45*UP)
        realizaciónDeltaPrima = MathTex(r"[A'\xrightarrow{x'} B'\xrightarrow{y'} C']").scale(0.5).set_color(NARANJA).move_to(círculoNaranja.get_center()).next_to(realizaciónDelta, DOWN)
        puntosNaranjas = MathTex(r"\dots").set_color(NARANJA).next_to(realizaciónDeltaPrima, DOWN)

        # Animación de la escena

        # Primera diapositiva
        self.next_section(type=PresentationSectionType.NORMAL)
        self.add(dominio)
        self.wait()

        self.next_section(type=PresentationSectionType.NORMAL)
        self.add(bifuntorAditivo)
        self.wait()

        self.next_section(type=PresentationSectionType.NORMAL)
        self.add(delta, deltaPrima)
        self.wait()

        self.next_section(type=PresentationSectionType.NORMAL)
        self.add(realizaciónAditiva)
        self.wait()

        self.next_section(type=PresentationSectionType.NORMAL)
        self.play(Transform(círculos.copy(), círculoNaranja))

        self.next_section(type=PresentationSectionType.NORMAL)
        self.play(Transform(delta.copy(), realizaciónDelta),
                  Transform(deltaPrima.copy(), realizaciónDeltaPrima),
                  )
        self.play(Write(puntosNaranjas))
        self.wait()

class Terminologia(MovingCameraScene):

    def construct(self):
        
        # Mobjects
        texto1 = Tex(r"\textbf{Definición}", " Consideremos una terna ", "$(\mathscr{A},\mathbb{E},\mathfrak{s})$").scale(escalaTexto).to_edge(LEFT, buff=buffTítulo+0.1).shift(2.9*UP)
        texto1.set_color_by_tex("Definición", NARANJA)
        texto1[2][1].set_color(GRIS)
        texto1[2][5].set_color(NARANJA)

        texto2 = Tex(r"(a) Un $\mathbb{E}$-\emph{triángulo} es un par $(A\xrightarrow{x}B\xrightarrow{y}C,\delta)$, donde la sucesión $A\xrightarrow{x}B\xrightarrow{y}C$\hfill\empty{}").next_to(texto1,DOWN, buff=buffRenglón).scale(escalaTexto).to_edge(LEFT)

        texto3 = Tex(r"realiza a $\delta\in\mathbb{E}(C,A)$, y lo denotamos por").next_to(texto2,DOWN, buff=buffTexto).scale(escalaTexto).to_edge(LEFT)

        ecuación1 = Tex(r"$A\xrightarrow{x}B\xrightarrow{y}C\xdashrightarrow{\delta}.$", tex_template=myTemplate).next_to(texto3, DOWN, buff=buffEcuación).scale(escalaTexto).set_x(0)

        texto4 = Tex(r"Esto \emph{no necesariamente} implica que $\delta$ sea un morfismo en ", "$\mathscr{A}$", " con dominio $C$.").next_to(ecuación1,DOWN, buff=2*buffEcuación).scale(escalaTexto).to_edge(LEFT)
        texto4[1].set_color(GRIS)

        texto5 = Tex(r"(b) Sean $A\xrightarrow{x}B\xrightarrow{y}C\xdashrightarrow{\delta}$ y $A'\xrightarrow{x'}B\xrightarrow{y'}C'\xdashrightarrow{\delta'}$ $\mathbb{E}$-triángulos. Un \emph{morfismo} ", tex_template=myTemplate).next_to(texto4,DOWN, buff=buffRenglón).scale(escalaTexto).to_edge(LEFT)

        texto6 = Tex(r"\emph{de} $\mathbb{E}$-\emph{triángulos} es una terna $(a,b,c)$ que realiza al morfismo de $\mathbb{E}$-extensiones").next_to(texto5,DOWN, buff=buffTexto).scale(escalaTexto).to_edge(LEFT)

        texto7 = Tex(r"$(a,c):\delta\to\delta'$ como en (", "1", "), y lo denotamos por").next_to(texto6,DOWN, buff=buffTexto).scale(escalaTexto).to_edge(LEFT)
        texto7[1].set_color(NARANJA)

        ecuación2 = SVGMobject("../Diagramas/Morfismo_de_E-triángulos.svg").set_color(WHITE).next_to(texto7,DOWN,buff=buffTikz/2).scale(escalaTexto).set_x(0)
        ecuación2[27:29].set_color(BLACK)
        ecuación2[38:42].set_color(BLACK)
        flechaDelta = DashedArrow(start=ecuación2[27].get_left()-[0.3,0,0], end=ecuación2[27].get_right()+[0.3,0,0], dash_length=0.2)
        flechaDeltaPrima = DashedArrow(start=ecuación2[38].get_left()-[0.3,0,0], end=ecuación2[38].get_right()+[0.3,0,0], dash_length=0.15)
        delta = Group(flechaDelta, MathTex("\delta").set_color(WHITE).scale(0.45).next_to(flechaDelta, UP, buff=0))
        deltaPrima = Group(flechaDeltaPrima, MathTex("\delta'").set_color(WHITE).scale(0.45).next_to(flechaDeltaPrima, DOWN, buff=0))
        ecuación2 = Group(ecuación2, delta, deltaPrima)

        texto8 = Tex(r"(c) Una \emph{conflación} es una sucesión $A\xrightarrow{x}B\xrightarrow{y}C$ que realiza a alguna $\mathbb{E}$-").next_to(ecuación2,DOWN,buff=buffTikz).scale(escalaTexto).to_edge(LEFT)

        texto9 = Tex(r"extensión $\delta\in\mathbb{E}(C,A)$.").next_to(texto8,DOWN, buff=buffTexto+0.05).scale(escalaTexto).to_edge(LEFT)

        texto10 = Tex(r"(d) Una \emph{inflación} es un morfismo $f$ en ", "$\mathscr{A}$", " que admite una conflación").next_to(texto9,DOWN, buff=5*buffRenglón).scale(escalaTexto).to_edge(LEFT)
        texto10[1].set_color(GRIS)

        texto11 = Tex(r"$A\xrightarrow{f}B\xrightarrow{}C$.").next_to(texto10,DOWN, buff=buffTexto).scale(escalaTexto).to_edge(LEFT)

        texto12 = Tex(r"(e) Una \emph{deflación} es un morfismo $f$ en ", "$\mathscr{A}$", " que admite una conflación").next_to(texto11,DOWN, buff=5*buffRenglón).scale(escalaTexto).to_edge(LEFT)
        texto12[1].set_color(GRIS)

        texto13 = Tex(r"$A\xrightarrow{}B\xrightarrow{f}C$.").next_to(texto12,DOWN, buff=buffTexto).scale(escalaTexto).to_edge(LEFT)

        textos = Group(texto1,texto2,texto3,ecuación1,texto4,texto5,texto6,texto7,texto8,texto9,texto10,texto11,texto12,texto13)
        textos.set_x(0)
        for i in range(1,14):
            if (i != 8) & (i != 9):
              textos[i].set_fill(opacity=0)
        recuadro = SurroundingRectangle(textos, stroke_color=NARANJA, buff=0.25)

        # Animación de la escena

        # Primera diapositiva
        self.next_section(type=PresentationSectionType.NORMAL)
        self.add_slide_frame("Definición de categoría extriangulada", "Terminología", 15)
        self.add(recuadro)
        self.add(textos)
        self.move_camera(ORIGIN)

        self.next_section(type=PresentationSectionType.NORMAL)
        texto2.set_fill(opacity=1)
        texto3.set_fill(opacity=1)
        ecuación1.set_fill(opacity=1)
        self.wait()

        self.next_section(type=PresentationSectionType.NORMAL)
        texto4.set_fill(opacity=1)
        self.wait()

        self.next_section(type=PresentationSectionType.NORMAL)
        texto5.set_fill(opacity=1)
        texto6.set_fill(opacity=1)
        texto7.set_fill(opacity=1)
        self.add(ecuación2)
        self.wait()

        self.next_section(type=PresentationSectionType.NORMAL)
        self.move_camera(4.15*DOWN)
        texto8.set_fill(opacity=1)
        texto9.set_fill(opacity=1)
        self.wait()

        self.next_section(type=PresentationSectionType.NORMAL)
        texto10.set_fill(opacity=1)
        texto11.set_fill(opacity=1)
        self.wait()

        self.next_section(type=PresentationSectionType.NORMAL)
        texto12.set_fill(opacity=1)
        texto13.set_fill(opacity=1)
        self.wait()

class CategoriaExtriangulada(MovingCameraScene):

    def construct(self):

        # Mobjects

        # (ET3)

        definición = Tex(r"\justifying \textbf{Definición} Una \emph{categoría pre-extriangulada} es una terna $(\mathscr{A},T,\Delta)$ tal que satisface los siguientes axiomas.").scale(escalaTexto).to_edge(LEFT, buff=buffTítulo+0.1).shift(2.7*UP).set_x(0)
        definición[0][0:10].set_color(NARANJA)
        definición[0][50].set_color(GRIS)
        definición[0][54].set_color(ROJO)
        T = definición[0][52].copy()
        Delta = definición[0][54].copy()
        definición[0][52].set_color(BLACK)
        definición[0][54].set_color(BLACK)
        copiaDefinición = definición.copy()
        copiaDefiniciónRojo = definición.copy()
        copiaDefiniciónRojo[0][0:10].set_color(ROJO)

        ET3_1 = Tex(r"(ET3) Sean $A \hspace{0.1mm} \to \hspace{0.1mm}  B \hspace{0.1mm} \to \hspace{0.1mm}  C \hspace{0.1mm} \xdashrightarrow{\delta}$ \hspace{1.5mm} y \hspace{1.5mm} $A' \hspace{0.1mm}\to \hspace{0.1mm} B' \hspace{0.1mm}\to \hspace{0.1mm} C' \hspace{0.1mm}\xdashrightarrow{\delta'}$ $\mathbb{E}$-triángulos. \hspace{3cm}", r"Entonces, para todo diagrama en ", "$\mathscr{A}$", tex_template=myTemplate).scale(escalaTexto).next_to(definición, DOWN, buff=3*buffEcuación).set_x(0)

        ET3_1[0].to_edge(LEFT, buff=1.5*buffIzquierdo)
        ET3_1[1].to_edge(LEFT, buff=1.5*buffIzquierdo)
        ET3_1[2].next_to(ET3_1[1][25], RIGHT, buff=0.3)
        ET3_1[2].set_color(GRIS)
        copiaET3_1 = ET3_1.copy()

        ET3_2 = SVGMobject("../Diagramas/Cuadrado_conmutativo_entre_E-triángulos.svg").next_to(ET3_1, DOWN, buff=buffTikz).set_color(WHITE)
        ET3_2[20:23].set_color(BLACK)
        ET3_2[27:31].set_color(BLACK)
        flechaDelta = DashedArrow(start=ET3_2[20].get_left()-[0.3,0,0], end=ET3_2[20].get_right()+[0.3,0,0], dash_length=0.2)
        flechaDeltaPrima = DashedArrow(start=ET3_2[27].get_left()-[0.3,0,0], end=ET3_2[27].get_right()+[0.3,0,0], dash_length=0.2)
        delta = Group(flechaDelta, MathTex("\delta").set_color(WHITE).scale(0.6).next_to(flechaDelta, UP, buff=0.05).shift(0.1*LEFT))
        deltaPrima = Group(flechaDeltaPrima, MathTex("\delta'").set_color(WHITE).scale(0.6).next_to(flechaDeltaPrima, DOWN, buff=0.05).shift(0.1*LEFT))
        ET3_2 = Group(ET3_2, delta, deltaPrima)
        copiaET3_2 = ET3_2.copy()

        ET3_3 = Tex(r"existe un morfismo $C\xrightarrow{c}C'$ en $\mathscr{A}$ tal que $(a,b,c)$ es un morfismo de $\mathbb{E}$-triángulos. triángulos", tex_template=myTemplate).scale(escalaTexto).next_to(ET3_2,DOWN,buff=buffTikz).to_edge(LEFT, buff=1.5*buffIzquierdo)
        ET3_3[0][23].set_color(GRIS)
        ET3_3[0][64:].set_color(BLACK)
        ET3_3[0][50:].to_edge(LEFT, buff=1.5*buffIzquierdo)
        copiaET3_3 = ET3_3.copy()

        ET3Dual = Tex(r"$(\text{ET3})^\ast$ Dual al anterior.").scale(escalaTexto).next_to(ET3_3, DOWN, buff=3*buffEcuación).to_edge(LEFT, buff=1.5*buffIzquierdo)

        # (TR3)

        pretriangulada = Tex("\emph{pretriangulada}").scale(escalaTexto).move_to(definición[0][23:39].get_center()).shift(0.1*LEFT)
        bifuntorAditivo = MathTex("\mathbb{E}").set_color(WHITE).move_to(definición[0][52].get_center()).scale(escalaTexto).shift(0.025*LEFT)
        copiaBifuntorAditivo = bifuntorAditivo.copy()
        realizaciónAditiva = MathTex("\mathfrak{s}").set_color(NARANJA).move_to(definición[0][54].get_center()).scale(escalaTexto).shift(0.05*DOWN)
        copiaRealizaciónAditiva = realizaciónAditiva.copy()
        TR3_1 = Tex(r"(TR3) Sean $X\to Y\to Z\to T(X)$ y $X'\to Y'\to Z'\to T(X')$ en $\Delta$.", tex_template=myTemplate).scale(escalaTexto).next_to(definición, DOWN, buff=4.65*buffEcuación).to_edge(LEFT, buff=1.5*buffIzquierdo)
        TR3_1[0][36].set_color(ROJO)
        puntos = MathTex(r"\dots")
        puntos.move_to(TR3_1[0:5].get_center()).to_edge(LEFT, buff=1.5*buffIzquierdo).shift(0.45*UP+0.2*RIGHT)
        TR3_2 = SVGMobject("../Diagramas/Cuadrado_conmutativo_entre_triángulos_distinguidos.svg").move_to(ET3_2.get_center()).set_color(WHITE)

        TR3_3 = Tex(r"existe un morfismo $Z\xrightarrow{h}Z'$ en $\mathscr{A}$ tal que $(f,g,h)$ es un morfismo de triángulos distinguidos.").scale(escalaTexto).move_to(ET3_3.get_center())
        TR3_3[0][24].set_color(GRIS)
        TR3_3[0][52:].to_edge(LEFT, buff=1.5*buffIzquierdo)

        # (ET4)

        extriangulada = Tex(r"\justifying Una categoría pre-extriangulada es \emph{extriangulada} si satisface los siguientes axiomas.").scale(escalaTexto).next_to(ET3Dual, DOWN, buff=2*buffTikz).to_edge(LEFT, buff=buffIzquierdo)
        copiaExtriangulada = extriangulada.copy()
        ET4_1 = Tex(r"\justifying (ET4) Cualesquiera dos inflaciones $A\xrightarrow{f}B$ y $B\xrightarrow{g}C$ se pueden completar a").scale(escalaTexto).next_to(extriangulada, DOWN, buff=2.75*buffEcuación).to_edge(LEFT, buff=1.5*buffIzquierdo)
        copiaET4_1 = ET4_1.copy()

        ET4_2 = SVGMobject("../Diagramas/Octaedro_extriangulado.svg").next_to(ET4_1, DOWN, buff=2*buffTikz).scale(1.5).set_color(WHITE)
        ET4_2[26:35].set_color(BLACK) #\delta
        ET4_2[50:55].set_color(BLACK) #\delta''
        ET4_2[55:59].set_color(BLACK) #\delta'
        ET4_2[61:73].set_color(BLACK) #\delta'''
        ET4_2[23:25].set_color(BLACK) #d
        ET4_2[47:49].set_color(BLACK) #e
        flechaDelta2 = DashedArrow(start=ET4_2[26].get_left()-[0.3,0,0], end=ET4_2[26].get_right()+[0.3,0,0], dash_length=0.2)
        flechaDeltaBiprima2 = DashedArrow(start=ET4_2[50].get_left()-[0.3,0,0], end=ET4_2[50].get_right()+[0.3,0,0], dash_length=0.2)
        flechaDeltaPrima2 = DashedArrow(start=ET4_2[55].get_top()+[0,0.3,0], end=ET4_2[55].get_bottom()-[0,0.3,0], dash_length=0.15)
        flechaDeltaTriprima2 = DashedArrow(start=ET4_2[61].get_top()+[0,0.3,0], end=ET4_2[61].get_bottom()-[0,0.3,0], dash_length=0.15)
        delta2 = Group(flechaDelta2, MathTex("\delta=\delta''\cdot d").set_color(WHITE).scale(0.45).next_to(flechaDelta2, UP, buff=0.05).shift(0.1*LEFT))
        deltaBiprima2 = Group(flechaDeltaBiprima2, MathTex("\delta''").set_color(WHITE).scale(0.45).next_to(flechaDeltaBiprima2, DOWN, buff=0.05).shift(0.1*LEFT))
        deltaPrima2 = Group(flechaDeltaPrima2, MathTex("\delta'").set_color(WHITE).scale(0.45).next_to(flechaDeltaPrima2, LEFT, buff=0.05))
        deltaTriprima2 = Group(flechaDeltaTriprima2, MathTex(r"\delta''' ", "= ", r"f'\cdot", r"\delta'").set_color(WHITE).scale(0.45).next_to(flechaDeltaTriprima2, RIGHT, buff=0.05))
        ET4_2[10].set_color(BLACK)
        ET4_2[60].set_color(BLACK)
        identidad1 = Group( Line(start=ET4_2[10].get_top()-[0.05,0,0], end=ET4_2[10].get_bottom()-[0.05,0,0]), Line(start=ET4_2[10].get_top()+[0.05,0,0], end=ET4_2[10].get_bottom()+[0.05,0,0]))
        identidad2 = Group( Line(start=ET4_2[60].get_left()+[0,0.05,0], end=ET4_2[60].get_right()+[0,0.05,0]), Line(start=ET4_2[60].get_left()-[0,0.05,0], end=ET4_2[60].get_right()-[0,0.05,0]))
        flecha_d = DashedArrow(start=ET4_2[23].get_top()+[0,0.3,0], end=ET4_2[23].get_bottom()-[0,0.3,0], dash_length=0.075)
        flecha_e = DashedArrow(start=ET4_2[47].get_top()+[0,0.3,0], end=ET4_2[47].get_bottom()-[0,0.3,0], dash_length=0.075)
        ET4_2 = Group(ET4_2, delta2, deltaBiprima2, deltaPrima2, deltaTriprima2, identidad1, identidad2, flecha_d, flecha_e)
        copiaET4_2 = ET4_2.copy()
        copiaFlechaDeltaBiprima2 = flechaDeltaBiprima2.copy()

        ET4_3 = Tex(r"\justifying donde ", "$f\cdot ..$ ", r"$\delta'' $", "$= $", r"$\delta'\cdot $", "$e$ ", r"y los dos renglones y las dos columnas con tres objetos \hfill\break son $\mathbb{E}$-triángulos.").scale(escalaTexto).next_to(ET4_2,DOWN,buff=buffTikz).to_edge(LEFT, buff=1.5*buffIzquierdo)
        ET4_3[1][2:4].set_fill(opacity=0)
        ET4_3[2:].shift(0.25*LEFT)
        ET4_3[6][45:].to_edge(LEFT, buff=1.5*buffIzquierdo)
        copiaET4_3 = ET4_3.copy()

        ET4Dual = Tex(r"$(\text{ET4})^\ast$ (Dual)").scale(escalaTexto).next_to(ET4_3, DOWN, buff=2.75*buffEcuación).to_edge(LEFT, buff=1.5*buffIzquierdo)
        ET4Dual.set_fill(opacity=0)

        # (TR4)

        pretriangulada2 = Tex("pretriangulada").scale(escalaTexto).set_color(WHITE).move_to(extriangulada[0][12:29].get_center())
        triangulada = Tex(r"\emph{triangulada}").scale(escalaTexto).set_color(WHITE).move_to(extriangulada[0][31:43].get_center())
        el = Tex("el").scale(escalaTexto).set_color(WHITE).move_to(extriangulada[0][56:58].get_center()).shift(0.05*UP+0.025*LEFT)
        punto = Tex(".").scale(escalaTexto).set_color(WHITE).move_to(extriangulada[0][75].get_center()).shift(0.06*DOWN+0.025*LEFT)
        TR4 = Tex("(TR4)").scale(escalaTexto).move_to(ET4_1[0][0:5].get_center())
        morfismos = Tex("morfismos ", r"$X\xrightarrow{u}Y$ ", "y ", r"$Y\xrightarrow{v}Z$").scale(escalaTexto).set_color(WHITE).move_to(ET4_1[0][20:40].get_center()).shift(0.05*DOWN+0.25*RIGHT) #Aquí tal vez "falten elementos" para Transform
        TR4_2 = SVGMobject("../Diagramas/Octaedro.svg").move_to(ET4_2.get_center()).set_color(WHITE).scale(1.5)
        TR4_2[34:36].set_stroke(opacity=0) # Identidad
        TR4_2[92:94].set_stroke(opacity=0) # Identidad
        identidad3 = Group( Line(start=TR4_2[35].get_top()-[0.05,0,0], end=TR4_2[35].get_bottom()-[0.05,0,0]), Line(start=TR4_2[35].get_top()+[0.05,0,0], end=TR4_2[35].get_bottom()+[0.05,0,0]))
        identidad4 = Group( Line(start=TR4_2[93].get_left()+[0,0.05,0], end=TR4_2[93].get_right()+[0,0.05,0]), Line(start=TR4_2[93].get_left()-[0,0.05,0], end=TR4_2[93].get_right()-[0,0.05,0]))
        identidad5 = Group( Line(start=TR4_2[58].get_top()-[0.05,0,0], end=TR4_2[58].get_bottom()-[0.05,0,0]), Line(start=TR4_2[58].get_top()+[0.05,0,0], end=TR4_2[58].get_bottom()+[0.05,0,0]))
        TR4_2[48:50].set_stroke(opacity=0) # a
        TR4_2[71:73].set_stroke(opacity=0) # b
        flecha_a = DashedArrow(start=TR4_2[48].get_top()+[0,0.3,0], end=TR4_2[48].get_bottom()-[0,0.3,0], dash_length=0.075)
        flecha_b = DashedArrow(start=TR4_2[71].get_top()+[0,0.3,0], end=TR4_2[71].get_bottom()-[0,0.3,0], dash_length=0.075)
        TR4_2 = Group(TR4_2, identidad3, identidad4, identidad5, flecha_a, flecha_b)
        cuatroObjetos = Tex("cuatro objetos").scale(escalaTexto).set_color(WHITE).move_to(ET4_3[6][37:44].get_center()).shift(0.05*RIGHT)
        triángulosDistinguidos = Tex("triángulos distinguidos.").scale(escalaTexto).set_color(WHITE).move_to(ET4_3[6][46:].get_center()).shift(1.15*RIGHT)

        # Recuadros
        recuadroNaranja = Group(definición, ET4Dual).surrounding_box(NARANJA)
        copiaRecuadroNaranja = recuadroNaranja.copy()
        recuadroRojo = Group(definición, ET4Dual).surrounding_box(ROJO)
        copiaRecuadroNaranja2 = copiaRecuadroNaranja.copy()
        copiaRecuadroRojo = recuadroRojo.copy()

        # Animación de la escena

        # Primera diapositiva
        self.next_section(type=PresentationSectionType.NORMAL)
        self.add(copiaRecuadroNaranja2, copiaRecuadroRojo, copiaRecuadroNaranja, recuadroRojo, recuadroNaranja)
        self.add(definición, bifuntorAditivo, realizaciónAditiva, extriangulada, ET4_1, ET4_2, ET4_3, ET4Dual)
        self.add_slide_frame("Definición de categoría extriangulada", "Categoría pre-extriangulada", 16)
        self.move_camera(ORIGIN)
        self.wait()

        self.next_section(type=PresentationSectionType.NORMAL)
        self.add(ET3_1, ET3_2, ET3_3)
        self.wait()

        self.next_section(type=PresentationSectionType.NORMAL)
        self.play(Uncreate(recuadroNaranja),
                  Transform(definición[0][0:10], copiaDefiniciónRojo[0][0:10]),
                  Transform(definición[0][22:39], pretriangulada),
                  Transform(bifuntorAditivo, T),
                  Transform(realizaciónAditiva, Delta),
                  Write(puntos),
                  Transform(ET3_1[0][1:4], TR3_1[0][1:4]),
                  Transform(ET3_1[0][9:20], TR3_1[0][9:20]),
                  Transform(ET3_1[0][20:33], TR3_1[0][20:33]),
                  Transform(ET3_1[0][33:], TR3_1[0][33:]),

                  Transform(ET3_2[0][0], TR3_2[0][0]),
                  Transform(ET3_2[0][1], TR3_2[1][0]),
                  Transform(ET3_2[0][2], TR3_2[2][0]),
                  Transform(ET3_2[0][3:5], TR3_2[7:9]),
                  Transform(ET3_2[0][5:7], TR3_2[9:11]),
                  Transform(ET3_2[0][7:9], TR3_2[11:13]),
                  Transform(ET3_2[0][9:12], TR3_2[18:21]),
                  Transform(ET3_2[0][12], TR3_2[21]),
                  Transform(ET3_2[0][13:15], TR3_2[22:24]),
                  Transform(ET3_2[0][15:18], TR3_2[24:27]),
                  Transform(ET3_2[0][18:20], TR3_2[27:29]),
                  Transform(ET3_2[1], TR3_2[29:31]),
                  Transform(ET3_2[0][23:25], TR3_2[37:39]),
                  Transform(ET3_2[0][25:27], TR3_2[39:41]),
                  Transform(ET3_2[2], TR3_2[41:43]),
                  Write(TR3_2[3:7]),
                  Write(TR3_2[13:18]),
                  Write(TR3_2[31:37]),

                  Transform(ET3_3[0][15:21], TR3_3[0][16:22]),
                  Transform(ET3_3[0][30:37], TR3_3[0][31:38]),
                  Transform(ET3_3[0][50:], TR3_3[0][52:]),
                  self.change_slide_subtitle("Categoría pretriangulada")
                  )
        self.wait()

        self.next_section(type=PresentationSectionType.NORMAL)
        self.play(Uncreate(recuadroRojo),
                  Transform(definición[0][0:10], copiaDefinición[0][0:10]),
                  Transform(definición[0][22:39], copiaDefinición[0][22:39]),
                  Transform(bifuntorAditivo, copiaBifuntorAditivo),
                  Transform(realizaciónAditiva, copiaRealizaciónAditiva),
                  Unwrite(puntos),
                  Transform(ET3_1[0][1:4], copiaET3_1[0][1:4]),
                  Transform(ET3_1[0][9:19], copiaET3_1[0][9:19]),
                  Transform(ET3_1[0][19:32], copiaET3_1[0][19:32]),
                  Transform(ET3_1[0][32:], copiaET3_1[0][32:]),

                  Transform(ET3_2[0][0], copiaET3_2[0][0]),
                  Transform(ET3_2[0][1], copiaET3_2[0][1]),
                  Transform(ET3_2[0][2], copiaET3_2[0][2]),
                  Transform(ET3_2[0][3:5], copiaET3_2[0][3:5]),
                  Transform(ET3_2[0][5:7], copiaET3_2[0][5:7]),
                  Transform(ET3_2[0][7:9], copiaET3_2[0][7:9]),
                  Transform(ET3_2[0][9:12], copiaET3_2[0][9:12]),
                  Transform(ET3_2[0][12], copiaET3_2[0][12]),
                  Transform(ET3_2[0][13:15], copiaET3_2[0][13:15]),
                  Transform(ET3_2[0][15:18], copiaET3_2[0][15:18]),
                  Transform(ET3_2[0][18:20], copiaET3_2[0][18:20]),
                  Transform(ET3_2[1], copiaET3_2[1]),
                  Transform(ET3_2[0][23:25], copiaET3_2[0][23:25]),
                  Transform(ET3_2[0][25:27], copiaET3_2[0][25:27]),
                  Transform(ET3_2[2], copiaET3_2[2]),
                  Unwrite(TR3_2[3:7]),
                  Unwrite(TR3_2[13:18]),
                  Unwrite(TR3_2[31:37]),

                  Transform(ET3_3[0][15:21], copiaET3_3[0][15:21]),
                  Transform(ET3_3[0][30:36], copiaET3_3[0][30:36]),
                  Transform(ET3_3[0][50:], copiaET3_3[0][50:]),
                  self.change_slide_subtitle("Categoría pre-extriangulada")
                  )
        self.wait()
 
        self.next_section(type=PresentationSectionType.NORMAL)
        self.add(ET3Dual)
        self.move_camera(ORIGIN)
        self.wait()
 
        self.next_section(type=PresentationSectionType.NORMAL)
        self.move_camera(7.65*DOWN)
        self.play(self.change_slide_subtitle("Categoría extriangulada"))
        self.wait()

        self.next_section(type=PresentationSectionType.NORMAL)
        extriangulada[0][67].set_fill(opacity=0)
        extriangulada[0][76:78].set_fill(opacity=0)
        self.play(Uncreate(copiaRecuadroNaranja),
                  Transform(extriangulada[0][12:29], pretriangulada2),
                  Transform(extriangulada[0][31:44], triangulada),
                  Transform(extriangulada[0][55:58], el),
                  Transform(extriangulada[0][75], punto),

                  Transform(ET4_1[0][0:5], TR4),
                  Transform(ET4_1[0][20:31], morfismos[0]),
                  Transform(ET4_1[0][31:36], morfismos[1]),
                  Transform(ET4_1[0][37:42], morfismos[3]),

                  Transform(ET4_2[0][0], TR4_2[0][0]),
                  Transform(ET4_2[0][1], TR4_2[0][1]),
                  Transform(ET4_2[0][2], TR4_2[0][2:4]),
                  Transform(ET4_2[0][3], TR4_2[0][8]),
                  Transform(ET4_2[0][4], TR4_2[0][9]),
                  Transform(ET4_2[0][5], TR4_2[0][10:12]),
                  Transform(ET4_2[0][7], TR4_2[0][16:18]),
                  Transform(ET4_2[0][8], TR4_2[0][18:20]),
                  Transform(ET4_2[0][12:15], TR4_2[0][37:40]),
                  Transform(ET4_2[0][15:18], TR4_2[0][40:43]),
                  Transform(ET4_2[0][19:23], TR4_2[0][44:48]),
                  Transform(ET4_2[7], TR4_2[4]), # Cambio de flecha d por flecha a
                  Transform(ET4_2[0][25], TR4_2[0][50]),
                  Transform(ET4_2[1][0], TR4_2[0][52:54]),
                  Transform(ET4_2[2][0], TR4_2[0][75:77]),
                  Transform(ET4_2[2][1], TR4_2[0][77:80]),
                  Transform(ET4_2[0][35:38], TR4_2[0][59:62]),
                  Transform(ET4_2[0][38:42], TR4_2[0][62:66]),
                  Transform(ET4_2[0][43:47], TR4_2[0][67:71]),
                  Transform(ET4_2[8], TR4_2[5]), # Cambio de flecha d por flecha a
                  Transform(ET4_2[0][49], TR4_2[0][73]),
                  Transform(ET4_2[0][50:55], TR4_2[0][75:77]),
                  Transform(ET4_2[3][0], TR4_2[0][86:88]),
                  Transform(ET4_2[3][1], TR4_2[0][88:91]),
                  Transform(ET4_2[4][0], TR4_2[0][94:96]),
                  Transform(ET4_2[4][1][0], TR4_2[0][96]),
                  Transform(ET4_2[4][1][1], TR4_2[0][91]),
                  Transform(ET4_2[4][1][2], TR4_2[0][104:109]),
                  Transform(ET4_2[4][1][3], TR4_2[0][88:91]),
                  Transform(ET4_2[5], TR4_2[1]),
                  Transform(ET4_2[6], TR4_2[2]),
                  Transform(ET4_2[1][1][0][0], TR4_2[0][54:57]),
                  Transform(ET4_2[0][11], TR4_2[0][36]),
                  Transform(ET4_2[0][18], TR4_2[0][43]),
                  Transform(ET4_2[0][42], TR4_2[0][66]),
                  Transform(ET4_2[1][1][0][1], TR4_2[0][51]),
                  Transform(ET4_2[1][1][0][2:6], TR4_2[0][77:80]),
                  Transform(ET4_2[1][1][0][6], TR4_2[0][50]),
                  Write(TR4_2[0][4:8]),
                  Write(TR4_2[0][12:16]),
                  Write(TR4_2[3][0]),
                  Write(TR4_2[3][1]),
                  Write(TR4_2[0][25:29]),
                  Write(TR4_2[0][102:104]),
                  Write(TR4_2[0][29:34]),
                  Transform(ET4_2[1][1][0][6], TR4_2[0][50]),

                  Transform(ET4_3[1], TR4_2[0][82:86]),
                  Transform(ET4_3[2], TR4_2[0][77:80]),
                  Transform(ET4_3[3], TR4_2[0][74]),
                  Transform(ET4_3[4], TR4_2[0][99:102]),
                  Transform(ET4_3[5], TR4_2[0][73]),
                  Write(TR4_2[0][80:82]),
                  Write(TR4_2[0][20:24]),
                  Write(TR4_2[0][97:99]),
                  Unwrite(ET4_3[6][0]),
                  Transform(ET4_2[0][6], TR4_2[0][24]), # Coma
                  Transform(ET4_3[6][34:45], cuatroObjetos), # Coma
                  Transform(ET4_3[6][48:], triángulosDistinguidos), # Coma
                  self.change_slide_subtitle("Categoría triangulada")
                  )
        self.wait()

        self.next_section(type=PresentationSectionType.NORMAL)
        extriangulada[0][67].set_fill(opacity=1)
        extriangulada[0][76:78].set_fill(opacity=1)
        self.play(Uncreate(copiaRecuadroRojo),
                  Transform(extriangulada[0][12:29], copiaExtriangulada[0][12:29]),
                  Transform(extriangulada[0][31:44], copiaExtriangulada[0][31:44]),
                  Transform(extriangulada[0][55:58], copiaExtriangulada[0][55:58]),
                  Transform(extriangulada[0][75], copiaExtriangulada[0][75]),

                  Transform(ET4_1[0][0:5], copiaET4_1[0][0:5]),
                  Transform(ET4_1[0][20:31], copiaET4_1[0][20:31]),
                  Transform(ET4_1[0][31:36], copiaET4_1[0][31:36]),
                  Transform(ET4_1[0][37:42], copiaET4_1[0][37:42]),
                  Transform(ET4_2[0][0], copiaET4_2[0][0]),
                  Transform(ET4_2[0][1], copiaET4_2[0][1]),
                  Transform(ET4_2[0][2], copiaET4_2[0][2]),
                  Transform(ET4_2[0][3], copiaET4_2[0][3]),
                  Transform(ET4_2[0][4], copiaET4_2[0][4]),
                  Transform(ET4_2[0][5], copiaET4_2[0][5]),
                  Transform(ET4_2[0][7], copiaET4_2[0][7]),
                  Transform(ET4_2[0][8], copiaET4_2[0][8]),
                  Transform(ET4_2[0][12:15], copiaET4_2[0][12:15]),
                  Transform(ET4_2[0][15:18], copiaET4_2[0][15:18]),
                  Transform(ET4_2[0][19:23], copiaET4_2[0][19:23]),
                  Transform(ET4_2[7], copiaET4_2[7]), # Cambio de flecha d por flecha a
                  Transform(ET4_2[0][25], copiaET4_2[0][25]),
                  Transform(ET4_2[1][0], copiaET4_2[1][0]),
                  Transform(ET4_2[2][0], copiaET4_2[2][0]),
                  Transform(ET4_2[2][1], copiaET4_2[2][1]),
                  Transform(ET4_2[0][35:38], copiaET4_2[0][35:38]),
                  Transform(ET4_2[0][38:42], copiaET4_2[0][38:42]),
                  Transform(ET4_2[0][43:47], copiaET4_2[0][43:47]),
                  Transform(ET4_2[8], copiaET4_2[8]), # Cambio de flecha d por flecha a
                  Transform(ET4_2[0][49], copiaET4_2[0][49]),
                  Transform(ET4_2[0][50:55], copiaET4_2[0][50:55]),
                  Transform(ET4_2[3][0], copiaET4_2[3][0]),
                  Transform(ET4_2[3][1], copiaET4_2[3][1]),
                  Transform(ET4_2[4][0], copiaET4_2[4][0]),
                  Transform(ET4_2[4][1][0], copiaET4_2[4][1][0]),
                  Transform(ET4_2[4][1][1], copiaET4_2[4][1][1]),
                  Transform(ET4_2[4][1][2], copiaET4_2[4][1][2]),
                  Transform(ET4_2[4][1][3], copiaET4_2[4][1][3]),
                  Transform(ET4_2[5], copiaET4_2[5]),
                  Transform(ET4_2[6], copiaET4_2[6]),
                  Transform(ET4_2[1][1][0][0], copiaET4_2[1][1][0][0]),
                  Transform(ET4_2[0][11], copiaET4_2[0][11]),
                  Transform(ET4_2[0][18], copiaET4_2[0][18]),
                  Transform(ET4_2[0][42], copiaET4_2[0][42]),
                  Transform(ET4_2[1][1][0][1], copiaET4_2[1][1][0][1]),
                  Transform(ET4_2[1][1][0][2:6], copiaET4_2[1][1][0][2:6]),
                  Transform(ET4_2[1][1][0][6], copiaET4_2[1][1][0][6]),
                  Unwrite(TR4_2[0][4:8]),
                  Unwrite(TR4_2[0][12:16]),
                  Unwrite(TR4_2[3][0]),
                  Unwrite(TR4_2[3][1]),
                  Unwrite(TR4_2[0][25:29]),
                  Unwrite(TR4_2[0][102:104]),
                  Unwrite(TR4_2[0][29:34]),
                  Transform(ET4_2[1][1][0][6], copiaET4_2[1][1][0][6]),
                  Write(copiaFlechaDeltaBiprima2),
                  Transform(ET4_3[1], copiaET4_3[1]),
                  Transform(ET4_3[2], copiaET4_3[2]),
                  Transform(ET4_3[3], copiaET4_3[3]),
                  Transform(ET4_3[4], copiaET4_3[4]),
                  Transform(ET4_3[5], copiaET4_3[5]),
                  Unwrite(TR4_2[0][80:84]),
                  Unwrite(TR4_2[0][20:24]),
                  Unwrite(TR4_2[0][97:99]),
                  Write(copiaET4_3[6][0]),
                  Transform(ET4_2[0][6], copiaET4_2[0][6]), # Coma
                  Transform(ET4_3[6][34:45], copiaET4_3[6][34:45]), # Coma
                  Transform(ET4_3[6][48:], copiaET4_3[6][48:]), # Coma
                  self.change_slide_subtitle("Categoría extriangulada")
                  )
        self.wait()


        self.next_section(type=PresentationSectionType.NORMAL)
        ET4Dual.set_fill(opacity=1)
        self.wait()

class Nota(MovingCameraScene):
    def construct(self):

        nota = Tex("Nota De ahora en adelante, ", "$(\mathscr{A},\mathbb{E},\mathfrak{s})$ denotará a una categoría extriangulada.").scale(escalaTexto).set_x(0)
        nota[0][0:4].set_color(NARANJA)
        nota[1][1].set_color(GRIS)
        nota[1][5].set_color(NARANJA)
        nota = Group(nota, nota.surrounding_box(NARANJA))

        self.next_section(type=PresentationSectionType.NORMAL)
        self.add_slide_frame("Definición de categoría extriangulada", "Categoría extriangulada", 17)
        self.add(nota)
        self.move_camera(ORIGIN)
