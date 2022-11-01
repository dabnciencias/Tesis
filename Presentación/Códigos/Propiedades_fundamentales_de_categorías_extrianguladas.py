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

# Comandos de LaTeX personalizados y paquetes TODO: Configurar el tex_template de un jalón para no tener que especificarlo muchas veces
myTemplate = TexTemplate(preamble=r"""
                                      \usepackage[spanish]{babel}
                                      \usepackage{amsmath}
                                      \usepackage{amssymb}
                         """)
myTemplate.add_to_preamble(r"""
                               \usepackage{ragged2e}
                               \usepackage{mathrsfs}
                               \newcommand{\xtwoheadrightarrow}[2][]{
                                 \xrightarrow[#1]{#2}\mathrel{\mkern-14mu}\rightarrow
                               }
                               \newcommand{\xrightarrowtail}[2][]{
                                 \xrightarrow[#1]{#2}\mathrel{\mkern-21mu}\rightarrowtail
                               }
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

def change_slide_number(self, númeroDiapositiva):
    nuevoNúmero = Tex(str(númeroDiapositiva)+"/"+númeroTotalDeDiapositivas).scale(escalaPieDePágina).align_on_border(DOWN+RIGHT, buff = 0.1).match_y(self.camera.frame[3][2])

    return Transform(self.camera.frame[3][2],nuevoNúmero)
MovingCameraScene.move_camera = move_camera
MovingCameraScene.add_slide_frame = add_slide_frame
MovingCameraScene.update_slide_frame = update_slide_frame
MovingCameraScene.change_slide_subtitle = change_slide_subtitle
MovingCameraScene.change_slide_number = change_slide_number

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

# Escenas

class SucesionExactaAsociada(MovingCameraScene):

    def construct(self):

        # Mobjects
        texto1 = Tex(r"\justifying \textbf{Proposición} ", r"Sean $A\xrightarrow{x} B\xrightarrow{y} C\xdashrightarrow{\delta}$ un $\mathbb{E}$-triángulo. Entonces, para todo $X\in\mathscr{A}$, se tiene que las sucesiones", tex_template=myTemplate).scale(escalaTexto).align_on_border(LEFT, buff=buffIzquierdo).shift(2.5*UP)
        texto1[0].set_color(NARANJA)
        texto1[1][51].set_color(GRIS)
        ecuación1 = Tex(r"$$\mathscr{A}(X,A) \xrightarrow{\mathscr{A}(X,x)} \mathscr{A}(X,B) \xrightarrow{\mathscr{A}(X,y)} \mathscr{A}(X,C) \xrightarrow{(\delta_\sharp)_X} \mathbb{E}(X,A) \xrightarrow{\mathbb{E}(X,x)} \mathbb{E}(X,B) \xrightarrow{\mathbb{E}(X,y)} \mathbb{E}(X,C),$$", r"$$\mathscr{A}(C,X) \xrightarrow{\mathscr{A}(y,X)} \mathscr{A}(B,X) \xrightarrow{\mathscr{A}(x,X)} \mathscr{A}(A,X) \xrightarrow{\delta^\sharp_X} \mathbb{E}(C,X) \xrightarrow{\mathbb{E}(y^\text{op},X)} \mathbb{E}(B,X) \xrightarrow{\mathbb{E}(x^\text{op},X)} \mathbb{E}(A,X)$$").scale(0.635).next_to(texto1, 1.5*DOWN).set_x(0)
        ecuación1[0][0].set_color(GRIS)
        ecuación1[0][6].set_color(GRIS)
        ecuación1[0][18].set_color(GRIS)
        ecuación1[0][24].set_color(GRIS)
        ecuación1[0][36].set_color(GRIS)
        ecuación1[1][0].set_color(GRIS)
        ecuación1[1][6].set_color(GRIS)
        ecuación1[1][18].set_color(GRIS)
        ecuación1[1][24].set_color(GRIS)
        ecuación1[1][36].set_color(GRIS)
        texto2 = Tex(r"\justifying son exactas en Ab, donde $\delta_\#$ y $\delta^\#$ son transformaciones naturales inducidas de $\delta\in\mathbb{E}(C,A)$ por el Lema de Yoneda, y $(\delta_\#)_X$ y $\delta^\#_X$ están dadas por").scale(escalaTexto).next_to(ecuación1, DOWN).align_on_border(LEFT, buff=buffIzquierdo)
        ecuación2 = Tex(r"$$(\delta_\sharp)_X: \mathscr{A}(X,C) \to \mathbb{E}(X,A), \ f\mapsto \delta\cdot f;$$", r"$$\delta_X^\sharp:\mathscr{A}(A,X) \to \mathbb{E}(C,X), \ g\mapsto g\cdot\delta.$$").scale(escalaTexto).next_to(texto2, 1.5*DOWN).set_x(0)
        ecuación2[0][6].set_color(GRIS)
        ecuación2[1][4].set_color(GRIS)
        ecuación2[1].shift(0.18*RIGHT)

        textos1 = Group(texto1, ecuación1, texto2, ecuación2)
        textos1 = Group(textos1.surrounding_box(NARANJA), textos1)

        texto3 = Tex(r"\justifying \textbf{Corolario} ", "Para cualquier morfismo de $\mathbb{E}$-triángulos").scale(escalaTexto).align_on_border(LEFT, buff=buffIzquierdo).shift(2.9*UP)
        texto3[0].set_color(NARANJA)
        ecuación3 = SVGMobject("./Morfismo_de_E-triángulos2.svg").set_color(WHITE).scale(escalaTexto).next_to(texto3, 1.5*DOWN).set_x(0)
        ecuación3[27:29].set_color(BLACK)
        ecuación3[38:42].set_color(BLACK)
        flechaDelta = DashedArrow(start=ecuación3[27].get_left()-[0.3,0,0], end=ecuación3[27].get_right()+[0.3,0,0], dash_length=0.2)
        flechaDeltaPrima = DashedArrow(start=ecuación3[38].get_left()-[0.3,0,0], end=ecuación3[38].get_right()+[0.3,0,0], dash_length=0.15)
        delta = Group(flechaDelta, MathTex("\delta").set_color(WHITE).scale(0.45).next_to(flechaDelta, UP, buff=0))
        deltaPrima = Group(flechaDeltaPrima, MathTex("\delta'").set_color(WHITE).scale(0.45).next_to(flechaDeltaPrima, DOWN, buff=0))
        texto4 = Tex(r"\justifying las siguientes condiciones son equivalentes. \begin{itemize} \item[(a)] $a$ se factoriza a través de $x$. \item[(b)] $a\cdot\delta = \delta'\cdot c = 0$. \item[(c)] $c$ se factoriza a través de $y$. \end{itemize}", r"Además, si cualesquiera dos de los morfismos $a, b$ y $c$ son isomorfismos en ", r"$\mathscr{A}$", ", entonces el tercero también lo es.").scale(escalaTexto).next_to(ecuación3, 1.5*DOWN).align_on_border(LEFT, buff=buffIzquierdo)
        texto4[2].set_color(GRIS)
        texto4[1:].set_fill(opacity=0)

        textos2 = Group(texto3, ecuación3, delta, deltaPrima, texto4)
        textos2 = Group(textos2.surrounding_box(NARANJA), textos2)

        # Animación de la escena

        # Primera diapositiva
        self.next_section(type=PresentationSectionType.NORMAL)
        self.add_slide_frame("Prop. fundamentales de cat. extrianguladas", "Sucesión exacta asociada", 18)
        self.add(textos1)
        self.move_camera(ORIGIN)

        self.next_section(type=PresentationSectionType.NORMAL)
        self.remove(textos1)
        self.add(textos2)
        self.play(self.change_slide_number(19))

        self.next_section(type=PresentationSectionType.NORMAL)
        texto4[1:].set_fill(opacity=1)
        self.wait()

class RelacionConCategoriasExactas(MovingCameraScene):

    def construct(self):

        # Mobjects
        ejem = Tex(r"\justifying \textbf{Ejemplo} Sea $(\mathscr{A},\mathscr{E})$ una categoría exacta. En caso de que $\text{Ext}^1(C,A)$ (obtenido siguiendo la construcción de Yoneda, como en categorías abelianas) sea un conjunto para cualesquiera $A,C\in\mathscr{A}$, definiendo a la realización $\mathfrak{s}(\delta)$ de $\delta=[A\xrightarrowtail{x} B\xtwoheadrightarrow{y} C]$ como $\delta$ mismo se demuestra que $(\mathscr{A}, \text{Ext}^1, \mathfrak{s})$ es una categoría extriangulada.", tex_template=myTemplate).scale(escalaTexto).align_on_border(LEFT, buff=buffIzquierdo).shift(1.75*UP).set_x(0)
        ejem[0][0:7].set_color(NARANJA)
        ejem[0][11].set_color(GRIS)
        ejem[0][13].set_color(AMARILLO)
        ejem[0][28:34].set_color(AMARILLO)
        ejem[0][158].set_color(GRIS)
        ejem[0][184].set_color(NARANJA)
        ejem[0][230].set_color(GRIS)
        ejem[0][237].set_color(NARANJA)
        ejem[0][255:268].set_color(NARANJA)
        ejem = Group(ejem.surrounding_box(NARANJA), ejem)

        coro = Tex(r"\justifying \textbf{Corolario} ", "Si ", r"$(\mathscr{A}, \mathbb{E}, \mathfrak{s})$ ", "es una categoría ", "extriangulada ", "en la cual toda inflación es un monomorfismo y toda deflación es un epimorfismo, y ", r"$\mathscr{S}$ ", r"es la clase de conflaciones dadas por los $\mathbb{E}$-triángulos, entonces ", r"$(\mathscr{A}, \mathscr{S})$ es una categoría exacta..").scale(escalaTexto).next_to(ejem, 2*DOWN).align_on_border(LEFT, buff=buffIzquierdo)
        coro[0].set_color(NARANJA)
        coro[2][1].set_color(GRIS)
        coro[2][5].set_color(NARANJA)
        coro[4].set_color(NARANJA)
        coro[6].set_color(AMARILLO)
        coro[8][2].set_color(GRIS)
        coro[8][4].set_color(AMARILLO)
        coro[8][20:26].set_color(AMARILLO)
        coro = Group(coro.surrounding_box(NARANJA), coro)

        textos = Group(ejem, coro)

        # Animación de la escena

        # Primera diapositiva
        self.next_section(type=PresentationSectionType.NORMAL)
        self.add_slide_frame("Prop. fundamentales de cat. extrianguladas", "Relación con categorías exactas", 20)
        self.add(ejem)
        self.move_camera(ORIGIN)

        self.next_section(type=PresentationSectionType.NORMAL)
        self.add(coro)
        self.wait()

class RelacionConCategoriasTrianguladas(MovingCameraScene):

    def construct(self):

        # Mobjects
        prop = Tex(r"\justifying \textbf{Proposición} Para una categoría aditiva $\mathscr{A}$, un automorfismo aditivo $T:\mathscr{A}\xrightarrow{\sim}\mathscr{A}$ y $\mathbf{E}^1(-,-):=\text{Hom}(-,T(-))$, las siguientes condiciones se satisfacen. \begin{itemize} \item[(a)] Sea $(\mathscr{A}, T, \Delta)$ una categoría trianguada. Si para cada $\delta\in\mathbf{E}^1(C,A)$ tomamos un triángulo distinguido $$A\xrightarrow{x} B\xrightarrow{y} C\xrightarrow{\delta} T(A)$$ y definimos $\mathfrak{s}(\delta):=[A\xrightarrow{x} B\xrightarrow{y} C]$, entonces $(\mathscr{A}, \mathbf{E}^1, \mathfrak{s})$ es extriangulada. \item[(b)] Supongamos que $(\mathscr{A}, \mathbf{E}^1, \mathfrak{s})$ es una categoría extriangulada. Si definimos una clase $\Delta$ como $$A\xrightarrow{x} B\xrightarrow{y} C\xrightarrow{\delta} T(A)\in\Delta \Leftrightarrow \mathfrak{s}(\delta) := [A\xrightarrow{x} B\xrightarrow{y} C],$$ entonces $(\mathscr{A}, T, \Delta)$ es una categoría triangulada. \end{itemize}", tex_template=myTemplate).scale(escalaTexto).align_on_border(LEFT, buff=buffIzquierdo).set_x(0)
        prop[0][0:12].set_color(NARANJA)
        prop[0][29:37].set_color(GRIS)
        prop[0][51:58].set_color(GRIS)
        prop[0][60].set_color(GRIS)
        prop[0][64].set_color(GRIS)
        prop[0][131].set_color(GRIS)
        prop[0][135].set_color(ROJO)
        prop[0][150:160].set_color(ROJO)
        prop[0][236].set_color(NARANJA)
        prop[0][263].set_color(GRIS)
        prop[0][268].set_color(NARANJA)
        prop[0][272:285].set_color(NARANJA)
        prop[0][303].set_color(GRIS)
        prop[0][308].set_color(NARANJA)
        prop[0][325:338].set_color(NARANJA)
        prop[0][357].set_color(ROJO)
        prop[0][379].set_color(ROJO)
        prop[0][381].set_color(NARANJA)
        prop[0][408].set_color(GRIS)
        prop[0][412].set_color(ROJO)
        prop[0][429:440].set_color(ROJO)
        prop[0][211:].shift(0.15*UP)
        prop[0][227:].shift(0.15*UP)
        prop[0][362:].shift(0.15*UP)
        prop[0][399:].shift(0.15*UP)
        prop = Group(prop.surrounding_box(NARANJA), prop).set_y(0)
        prop[1][0][124:].set_fill(opacity=0)

        # Animación de la escena

        # Primera diapositiva
        self.next_section(type=PresentationSectionType.NORMAL)
        self.add_slide_frame("Prop. fundamentales de cat. extrianguladas", "Relación con categorías trianguladas", 21)
        self.add(prop)
        self.move_camera(ORIGIN)

        self.next_section(type=PresentationSectionType.NORMAL)
        prop[1][0][124:286].set_fill(opacity=1)
        self.wait()

        self.next_section(type=PresentationSectionType.NORMAL)
        prop[1][0][286:].set_fill(opacity=1)
        self.wait()

class ObjetosProyectivosEInyectivos(MovingCameraScene):

    def construct(self):

        # Mobjects
        defi_1 = Tex(r"\justifying \textbf{Definición} Un objeto $P\in\mathscr{A}$ es $\mathbb{E}$-\emph{proyectivo} si para todo diagrama en $\mathscr{A}$ de la forma ", tex_template=myTemplate).scale(escalaTexto).align_on_border(LEFT, buff=buffIzquierdo).shift(2.5*UP).set_x(0)
        defi_1[0][0:10].set_color(NARANJA)
        defi_1[0][20].set_color(GRIS)
        defi_1[0][55].set_color(GRIS)
        ecuación1 = SVGMobject("./E-proyectivo.svg").next_to(defi_1, DOWN).scale(escalaTexto).set_color(WHITE)
        ecuación1[13:].set_color(BLACK)
        flechaDelta = DashedArrow(start=ecuación1[13].get_left()-[0.3,0,0], end=ecuación1[13].get_right()+[0.3,0,0], dash_length=0.2)
        delta = Group(flechaDelta, MathTex("\delta").set_color(WHITE).scale(0.45).next_to(flechaDelta, UP, buff=0))
        defi_2 = Tex(r"\justifying se tiene que $f$ se factoriza a través de $y$. Denotaremos por $\text{Proj}_\mathbb{E}(\mathscr{A})$ a la clase de los objetos $\mathbb{E}$-proyectivos en $\mathscr{A}$. La categoría $\mathscr{A}$ tiene \emph{suficientes} $\mathbb{E}$-\emph{proyectivos} si para cualquier $X\in\mathscr{A}$ existe una deflación $P\to X$, con $P\in\text{Proj}_\mathbb{E}(\mathscr{A})$.", tex_template=myTemplate).scale(escalaTexto).next_to(ecuación1, DOWN).align_on_border(LEFT, buff=buffIzquierdo).set_x(0)
        defi_2[0][54].set_color(GRIS)
        defi_2[0][91].set_color(GRIS)
        defi_2[0][105].set_color(GRIS)
        defi_2[0][151].set_color(GRIS)
        defi_2[0][185].set_color(GRIS)
        defi_2[0][34:].set_fill(opacity=0)

        defi = Group(defi_1, ecuación1, delta, defi_2)
        defi = Group(defi.surrounding_box(NARANJA), defi)

        prop = Tex(r"\justifying \textbf{Proposición} Un objeto $P\in\mathscr{A}$ es $\mathbb{E}$-proyectivo si, y sólo si, se satisface que $\mathbb{E}(P,A)=0$ para cualquier $A\in\mathscr{A}$.").scale(escalaTexto).next_to(defi, 2*DOWN).align_on_border(LEFT, buff=buffIzquierdo)
        prop[0][0:11].set_color(NARANJA)
        prop[0][21].set_color(GRIS)
        prop[0][84].set_color(GRIS)
        prop = Group(prop.surrounding_box(NARANJA), prop)

        textos = Group(defi, prop)

        # Animación de la escena

        # Primera diapositiva
        self.next_section(type=PresentationSectionType.NORMAL)
        self.add_slide_frame("Prop. fundamentales de cat. extrianguladas", "Objetos proyectivos e inyectivos", 22)
        self.add(defi)
        self.move_camera(ORIGIN)

        self.next_section(type=PresentationSectionType.NORMAL)
        defi_2[0][34:93].set_fill(opacity=1)
        self.wait()

        self.next_section(type=PresentationSectionType.NORMAL)
        defi_2[0][93:].set_fill(opacity=1)
        self.wait()

        self.next_section(type=PresentationSectionType.NORMAL)
        self.add(prop)
        self.wait()

class CategoriasExtrianguladasCociente(MovingCameraScene):

    def construct(self):

        # Mobjects
        prop = Tex(r"\justifying \textbf{Proposición} Sea $\mathscr{I}\subseteq\mathscr{A}$ una subcategoría aditiva plena de $\mathscr{A}$. Si $\mathscr{I}\subseteq\text{Proj}_\mathbb{E}(\mathscr{A})\cap\text{Inj}_\mathbb{E}(\mathscr{A})$, entonces la categoría cociente $\mathscr{A}/\mathscr{I}$ tiene una estructura de categoría extriangulada, inducida de la de $\mathscr{A}$.", tex_template=myTemplate).scale(escalaTexto).align_on_border(LEFT, buff=buffIzquierdo).shift(2.25*UP).set_x(0)
        prop[0][0:12].set_color(NARANJA)
        prop[0][15].set_color(GRIS)
        prop[0][17].set_color(GRIS)
        prop[0][34:41].set_color(GRIS)
        prop[0][48].set_color(GRIS)
        prop[0][52].set_color(GRIS)
        prop[0][60].set_color(GRIS)
        prop[0][68].set_color(GRIS)
        prop[0][99:102].set_color(GRIS)
        prop[0][132:145].set_color(NARANJA)
        prop[0][160].set_color(GRIS)
        prop = Group(prop.surrounding_box(NARANJA), prop)

        coro = Tex(r"\justifying \textbf{Corolario} Sea $\mathscr{I}\subseteq\mathscr{A}$ una subcategoría aditiva plena de $\mathscr{A}$ tal que $$\mathbb{E}(\mathscr{I}, \mathscr{I})=0.$$ Si $\mathscr{Z}\subseteq\mathscr{A}$ es la subcategoría de los objetos $Z\in\mathscr{A}$ tales que $$\mathbb{E}(Z,I) = 0 = \mathbb{E}(I,Z) \quad \forall \ I\in\mathscr{I},$$ entonces $\mathscr{Z}/\mathscr{I}$ tiene una estructura de categoría extriangulada.").scale(escalaTexto).next_to(prop, 2*DOWN).align_on_border(LEFT, buff=buffIzquierdo)
        coro[0][0:9].set_color(NARANJA)
        coro[0][12].set_color(GRIS)
        coro[0][14].set_color(GRIS)
        coro[0][30:37].set_color(GRIS)
        coro[0][44].set_color(GRIS)
        coro[0][53].set_color(GRIS)
        coro[0][55].set_color(GRIS)
        coro[0][62].set_color(GRIS)
        coro[0][64].set_color(GRIS)
        coro[0][95].set_color(GRIS)
        coro[0][122].set_color(GRIS)
        coro[0][132:135].set_color(GRIS)
        coro[0][164:177].set_color(NARANJA)
        coro = Group(coro.surrounding_box(NARANJA), coro)

        textos = Group(prop, coro)

        # Animación de la escena

        # Primera diapositiva
        self.next_section(type=PresentationSectionType.NORMAL)
        self.add_slide_frame("Prop. fundamentales de cat. extrianguladas", "Categorías extrianguladas cociente", 23)
        self.add(prop)
        self.move_camera(ORIGIN)

        self.next_section(type=PresentationSectionType.NORMAL)
        self.add(coro)
        self.wait()

class ParesDeCotorsionCompletos(MovingCameraScene):

    def construct(self):

        # Mobjects
        pdcc = Tex(r"\justifying \textbf{Definición} ", r"Un \emph{par de cotorsión (completo)} $(\mathcal{U}, \mathcal{V})$ en ", r"$(\mathscr{A}, \mathbb{E}, \mathfrak{s})$ ", r"es un par $(\mathcal{U}, \mathcal{V})$ de subcategorías ", "aditivas ", "plenas de ", r"$\mathscr{A}$", ", cerradas por sumandos directos en ", r"$\mathscr{A}$, ", "tal que cumple las siguientes condiciones.", r"\begin{itemize} \item[(1)] $\mathbb{E}(\mathcal{U}, \mathcal{V}) = 0$. \item[(2)] Para cualquier $C\in\mathscr{A}$, existe una conflación $V^C\to U^C\to C$ tal que $U^C\in\mathcal{U}$ y $V^C\in\mathcal{V}$. \item[(3)] Para cualquier $C\in\mathscr{A}$, existe una conflación $C\to V_C\to U_C$ tal que $U_C\in\mathcal{U}$ y $V_C\in\mathcal{V}$. \end{itemize}").scale(escalaTexto).shift(0.75*UP).align_on_border(LEFT, buff=buffIzquierdo)
        pdcc[0].set_color(NARANJA)
        pdcc[2][1].set_color(GRIS)
        pdcc[2][5].set_color(NARANJA)
        pdcc[4].set_color(GRIS)
        pdcc[6].set_color(GRIS)
        pdcc[8][0].set_color(GRIS)
        pdcc[10][30].set_color(GRIS)
        pdcc[10][41:51].set_color(NARANJA)
        pdcc[10][92].set_color(GRIS)
        pdcc[10][103:113].set_color(NARANJA)
        pdcc = Group(pdcc.surrounding_box(NARANJA), pdcc)

        self.next_section(type=PresentationSectionType.NORMAL)
        self.add_slide_frame("Prop. fundamentales de cat. extrianguladas", "Pares de cotorsión completos", 24)
        self.add(pdcc)
        self.move_camera(ORIGIN)
