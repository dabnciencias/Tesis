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

class Introduccion(MovingCameraScene):

    def construct(self):

        # Diapositiva 3/?
        noción = Tex(r"\justifying En 1979, Salce", "[1] ", "introdujo la noción de \emph{pares de cotorsión} en la categoría de grupos abelianos ", "Ab ", "haciendo la siguiente").scale(escalaTexto).align_on_border(LEFT, buff=0.5).shift(2.25*UP)
        noción[1][1].set_color(VERDE)
        noción[3][:].set_color(AZUL)
        obs_1 = Tex(r"\justifying \textbf{Observación} ", r"Para $S\subseteq\text{Ab}$, la clase de los grupos abelianos $V$ tales que todo $S\in\mathcal{S}$ es proyectivo con respecto a todas las sucesiones exactas de la forma").scale(escalaTexto).next_to(noción, 2.5*DOWN).align_on_border(LEFT, buff=buffIzquierdo)
        obs_1[0][:].set_color(AZUL)
        obs_1[1][6:8].set_color(AZUL)
        ecuación1 = MathTex(r"0\to V\to W\to Y\to 0").scale(escalaTexto).next_to(obs_1, 1.25*DOWN)
        obs_2 = Tex(r"se puede caracterizar con el funtor ", r"$\text{Ext}^1_\mathbb{Z}$ como sigue:").scale(escalaTexto).next_to(ecuación1, 1.25*DOWN).align_on_border(LEFT, buff=buffIzquierdo)
        obs_2[1][4].set_color(AZUL)
        ecuación2 = MathTex(r"\big\{ V\in\text{Ab} \mid ", r"\text{Ext}^1_\mathbb{Z} (S,V) = 0 \quad \forall \ S\in\mathcal{S} \big\}.").scale(escalaTexto).next_to(obs_2, 1.25*DOWN).set_x(0)
        ecuación2[0][3:5].set_color(AZUL)
        ecuación2[1][4].set_color(AZUL)
        recuadro = Group(obs_1, ecuación1, obs_2, ecuación2).surrounding_box(AZUL)
        dual = Tex("\justifying Más aún, notó que la observación dual también es válida.").scale(escalaTexto).next_to(ecuación2, 2.5*DOWN).align_on_border(LEFT, buff=0.5)
        textos1 = Group(noción, obs_1, ecuación1, obs_2, ecuación2, recuadro)

        self.next_section(type=PresentationSectionType.NORMAL)
        self.add_slide_frame("Introducción", "Ab", 3)
        self.camera.frame[2][1][:].set_color(AZUL)
        self.add(textos1)
        self.move_camera(ORIGIN)

        self.next_section(type=PresentationSectionType.NORMAL)
        self.add(dual)
        self.wait()

        # Diapositiva 4/?

        pdcAb = Tex(r"\justifying \textbf{Definición} ", r"Un \emph{par de cotorsión} $(\mathcal{U}, \mathcal{V})$ en ", "Ab ", r"es un par $(\mathcal{U}, \mathcal{V})$ de subcategorías plenas de ", "Ab ", "que cumple las siguientes condiciones.", r"\begin{enumerate} \item[(1)] $\text{Ext}^1_\mathbb{Z} (\mathcal{U}, \mathcal{V}) = 0$. \item[(2)] $\text{Ext}^1_\mathbb{Z} (U, X) = 0 \quad \forall \ U\in\mathcal{U} \Rightarrow X\in\mathcal{V}$. \item[(3)] $\text{Ext}^1_\mathbb{Z} (Z, V) = 0 \quad \forall \ V\in\mathcal{V} \Rightarrow Z\in\mathcal{U}$. \end{enumerate}").scale(escalaTexto).shift(1.5*UP).align_on_border(LEFT, buff=buffIzquierdo)
        pdcAb[0].set_color(AZUL)
        pdcAb[2].set_color(AZUL)
        pdcAb[4].set_color(AZUL)
        pdcAb[6][7].set_color(AZUL)
        pdcAb[6][23].set_color(AZUL)
        pdcAb[6][47].set_color(AZUL)
        pdcAb = Group (pdcAb.surrounding_box(AZUL), pdcAb)

        ObsAb = Tex(r"\justifying \textbf{Observación} ", "Las condiciones anteriores equivalen a las siguientes.", r"\begin{itemize} \item[$(\ast)$] $Z\in\mathcal{U} \Leftrightarrow \text{Ext}^1_\mathbb{Z}(Z,V)=0 \quad \forall \ V\in\mathcal{V}. \quad (\mathcal{U} = {}^{\perp_1}\mathcal{V})$ \item[$(\ast\ast)$] $X\in\mathcal{V} \Leftrightarrow \text{Ext}^1_\mathbb{Z}(U,X)=0 \quad \forall \ U\in\mathcal{U}. \quad (\mathcal{V} = \mathcal{U}^{\perp_1} )$ \end{itemize}").scale(escalaTexto).shift(1.75*DOWN).align_on_border(LEFT, buff=buffIzquierdo)
        ObsAb[0].set_color(AZUL)
        ObsAb[2][11].set_color(AZUL)
        ObsAb[2][43].set_color(AZUL)
        ObsAb[2][24:31].set_fill(opacity=0)
        ObsAb[2][56:].set_fill(opacity=0)
        ObsAb = Group(ObsAb.surrounding_box(AZUL), ObsAb)

        self.next_section(type=PresentationSectionType.NORMAL)
        textos1[0][:].set_fill(opacity=0)
        textos1[1][:].set_fill(opacity=0)
        textos1[2][:].set_fill(opacity=0)
        textos1[3][:].set_fill(opacity=0)
        textos1[4][:].set_fill(opacity=0)
        textos1[5][:].set_stroke(opacity=0)
        dual[:].set_fill(opacity=0)
        self.add(pdcAb)
        self.play(self.change_slide_number(4))

        self.next_section(type=PresentationSectionType.NORMAL)
        self.add(ObsAb)
        self.wait()

        self.next_section(type=PresentationSectionType.NORMAL)
        ObsAb[1][2][24:31].set_fill(opacity=1)
        ObsAb[1][2][56:].set_fill(opacity=1)
        self.wait()

        # Abelianas

        pdcB = Tex(r"\justifying \textbf{Definición} ", r"Un \emph{par de cotorsión} $(\mathcal{U}, \mathcal{V})$ en ", r"$\mathscr{B}$", r"es un par $(\mathcal{U}, \mathcal{V})$ de subcategorías plenas de ", r"$\mathscr{B}$ ", "que cumple las siguientes condiciones.", r"\begin{enumerate} \item[(1)] $\text{Ext}^1_\mathscr{B} (\mathcal{U}, \mathcal{V}) = 0$. \item[(1)] $\text{Ext}^1_\mathscr{B} (U, X) = 0 \quad \forall \ U\in\mathcal{U} \Rightarrow X\in\mathcal{V}$. \item[(1)] $\text{Ext}^1_\mathscr{B} (Z, V) = 0 \quad \forall \ V\in\mathcal{V} \Rightarrow Z\in\mathcal{U}$. \end{enumerate}").scale(escalaTexto).shift(1.5*UP).align_on_border(LEFT, buff=buffIzquierdo)
        pdcB[2].set_color(AZUL).shift(0.1*LEFT)
        pdcB[4].set_color(AZUL).shift(0.05*RIGHT)
        pdcB[6][7].set_color(AZUL).scale(0.9).shift(0.05*LEFT)
        pdcB[6][23].set_color(AZUL).scale(0.9).shift(0.05*LEFT)
        pdcB[6][47].set_color(AZUL).scale(0.9).shift(0.05*LEFT)
        pdcB = Group (pdcB.surrounding_box(AZUL), pdcB)

        ObsB = Tex(r"\justifying \textbf{Observación} ", "Las condiciones anteriores equivalen a las siguientes.", r"\begin{itemize} \item[$(\ast)$] $Z\in\mathcal{U} \Leftrightarrow \text{Ext}^1_\mathscr{B}(Z,V)=0 \quad \forall \ V\in\mathcal{V}. \quad (\mathcal{U} = {}^{\perp_1}\mathcal{V})$ \item[$(\ast\ast)$] $X\in\mathcal{V} \Leftrightarrow \text{Ext}^1_\mathscr{B}(U,X)=0 \quad \forall \ U\in\mathcal{U}. \quad (\mathcal{V} = \mathcal{U}^{\perp_1} )$ \end{itemize}").scale(escalaTexto).shift(1.75*DOWN).align_on_border(LEFT, buff=buffIzquierdo)
        ObsB[0].set_color(AZUL)
        ObsB[2][11].set_color(AZUL).scale(0.9).shift(0.05*LEFT)
        ObsB[2][43].set_color(AZUL).scale(0.9).shift(0.05*LEFT)
        ObsB[2][24:31].set_fill(opacity=0)
        ObsB[2][56:].set_fill(opacity=0)
        ObsB = Group(ObsB.surrounding_box(AZUL), ObsB)

        self.next_section(type=PresentationSectionType.NORMAL)
        self.play(self.change_slide_subtitle("Abelianas",AZUL),
                  Transform(pdcAb[1][2], pdcB[1][2]),
                  Transform(pdcAb[1][4], pdcB[1][4]),
                  Transform(pdcAb[1][6][7], pdcB[1][6][7]),
                  Transform(pdcAb[1][6][23], pdcB[1][6][23]),
                  Transform(pdcAb[1][6][47], pdcB[1][6][47]),
                  Transform(ObsAb[1][2][11], ObsB[1][2][11]),
                  Transform(ObsAb[1][2][43], ObsB[1][2][43])
                  )
        self.wait()

        # Diapositiva 5/?

        completo = Tex(r"\flushleft Más aún, $(\mathcal{U}, \mathcal{V})$ es \emph{completo} si cumple las siguientes condiciones.", r"\begin{itemize} \item[(4)] Para cualquier $C\in\mathscr{B}$, existe una sucesión exacta corta $0\to V^C\to U^C\to C\to 0$ tal que $U^C\in\mathcal{U}$ y $V^C\in\mathcal{V}$. \item[(5)] Para cualquier $C\in\mathscr{B}$, existe una sucesión exacta corta $0\to C\to V_C\to U_C\to 0$ tal que $U_C\in\mathcal{U}$ y $V_C\in\mathcal{V}$. \end{itemize}").scale(escalaTexto).align_on_border(LEFT, buff=buffIzquierdo).shift(1.8*DOWN)
        completo[1][18].set_color(AZUL)
        completo[1][93].set_color(AZUL)
        completo[1][29:48].set_color(AZUL)
        completo[1][104:123].set_color(AZUL)
        recuadroCompleto = Group(pdcAb[1], completo).surrounding_box(AZUL)

        self.next_section(type=PresentationSectionType.NORMAL)
        pdcAb[0].set_stroke(opacity=0)
        ObsAb[0].set_stroke(opacity=0)
        ObsAb[1].set_fill(opacity=0)
        self.add(recuadroCompleto, completo)
        self.play(self.change_slide_number(5))

        # Exactas

        pdccEx = Tex(r"\justifying \textbf{Definición} ", r"Un \emph{par de cotorsión (completo)} $(\mathcal{U}, \mathcal{V})$ en ", r"$(\mathscr{A}, \mathscr{E})$ ", r"es un par $(\mathcal{U}, \mathcal{V})$ de subcategorías plenas de ", r"$\mathscr{A}$", ", cerradas por sumandos directos en ", r"$\mathscr{A}$, ", "tal que cumple las siguientes condiciones.", r"\begin{itemize} \item[(1)] $\text{Ext}^1_{(\mathscr{A}, \mathscr{E})}(\mathcal{U}, \mathcal{V}) = 0$. \item[(2)] Para cualquier $C\in\mathscr{A}$, existe una sucesión exacta corta $V^C\to U^C\to C$ tal que $U^C\in\mathcal{U}$ y $V^C\in\mathcal{V}$. \item[(3)] Para cualquier $C\in\mathscr{A}$, existe una sucesión exacta corta $C\to V_C\to U_C$ tal que $U_C\in\mathcal{U}$ y $V_C\in\mathcal{V}$. \end{itemize}").scale(escalaTexto).shift(0.75*UP).align_on_border(LEFT, buff=buffIzquierdo)
        pdccEx[0].set_color(AMARILLO)
        pdccEx[2].set_color(AMARILLO)
        pdccEx[4].set_color(GRIS)
        pdccEx[6][0].set_color(GRIS)
        pdccEx[8][7:12].set_color(AMARILLO)
        pdccEx[8][38].set_color(GRIS)
        pdccEx[8][49:68].set_color(AMARILLO)
        pdccEx[8][109].set_color(GRIS)
        pdccEx[8][120:139].set_color(AMARILLO)
        pdccEx = Group (pdccEx.surrounding_box(AMARILLO), pdccEx)

        self.next_section(type=PresentationSectionType.NORMAL)
        pdcAb[1].set_fill(opacity=0)
        completo.set_fill(opacity=0)
        recuadroCompleto.set_stroke(opacity=0)
        self.add(pdccEx)
        self.play(self.change_slide_subtitle("Exactas", color=AMARILLO), run_time=0.01)
        self.wait()

        # Trianguladas

        pdccTr = Tex(r"\justifying \textbf{Definición} ", r"Un \emph{par de cotorsión (completo)} $(\mathcal{U}, \mathcal{V})$ en ", r"$(\mathscr{A}, T, \Delta)$ ", r"es un par $(\mathcal{U}, \mathcal{V})$ de subcategorías aditivas plenas de ", r"$\mathscr{A}$", ", cerradas por sumandos directos en ", r"$\mathscr{A}$, ", "tal que cumple las siguientes condiciones.", r"\begin{itemize} \item[(1)] $\text{Ext}^1_{(\mathscr{A}, T, \Delta)}(\mathcal{U}, \mathcal{V}) = 0$. \item[(2)] Para cualquier $C\in\mathscr{A}$, existe un triángulo distinguido $V\to U\to C\to T(V)$ tal que $U\in\mathcal{U}$ y $V\in\mathcal{V}$. \end{itemize}").scale(escalaTexto).shift(1.25*UP).align_on_border(LEFT, buff=buffIzquierdo)
        pdccTr[0].set_color(ROJO)
        pdccTr[2].set_color(ROJO)
        pdccTr[3][27:35].set_color(GRIS)
        pdccTr[4].set_color(GRIS)
        pdccTr[6][0].set_color(GRIS)
        pdccTr[8][7:14].set_color(ROJO)
        pdccTr[8][40].set_color(GRIS)
        pdccTr[8][50:70].set_color(ROJO)
        pdccTr = Group (pdccTr.surrounding_box(ROJO), pdccTr)

        self.next_section(type=PresentationSectionType.NORMAL)
        self.remove(pdccEx)
        self.add(pdccTr)
        self.play(self.change_slide_subtitle("Trianguladas", color=ROJO), run_time=0.01)
        self.wait()

class Categorias(MovingCameraScene):
    
    def construct(self):

        Trianguladas = Group(Tex("Trianguladas"), Ellipse(width=3.75, height=1)).set_color(ROJO).align_on_border(UP+LEFT, buff=0.25)
        Trianguladas = Group(SurroundingRectangle(Trianguladas, color=BLACK, fill_opacity=1), Trianguladas)
        Semisimples = Group(Tex("Semisimples"), Ellipse(width=3.75, height=1)).set_color(MAGENTA).align_on_border(UP+RIGHT, buff=0.25).set_y(Trianguladas.get_center()[1])
        Aditivas = Group(Tex("Aditivas"), Ellipse(width=2.5, height=1)).set_color(GRIS).align_on_border(DOWN+LEFT, buff=0.25).set_x(Trianguladas.get_center()[0])
        Abelianas = Group(Tex("Abelianas"), Ellipse(width=3, height=1)).set_color(AZUL).align_on_border(DOWN+RIGHT, buff=0.25).set_x(Semisimples.get_center()[0])
        Abelianas = Group(SurroundingRectangle(Abelianas, color=BLACK, fill_opacity=1), Abelianas)
        Exactas = Group(Tex("Exactas"), Ellipse(width=2.5, height=1)).set_color(AMARILLO).align_on_border(DOWN, buff=0.25)
        Exactas = Group(SurroundingRectangle(Exactas, color=BLACK, fill_opacity=1), Exactas)
        Extrianguladas = Group(Tex("Extrianguladas"), Ellipse(width=4.25, height=1)).set_color(NARANJA).move_to([(Aditivas.get_center()[0]+Exactas.get_center()[0])/2, (Trianguladas.get_center()[1]+Aditivas.get_center()[1])/2, 0])
        eje_horizontal = DashedLine(Aditivas.get_edge_center(RIGHT), Abelianas.get_edge_center(RIGHT), buff=0.1, dash_length=0.15)
        eje_vertical = DashedLine(Aditivas.get_edge_center(UP), Trianguladas.get_edge_center(UP), buff=0.1, dash_length=0.15)

        # Primera diapositiva
        self.next_section(type=PresentationSectionType.NORMAL)
        self.add(Aditivas, eje_horizontal, eje_vertical)
        self.wait()

        self.next_section(type=PresentationSectionType.NORMAL)
        self.add(Abelianas)
        self.wait()

        self.next_section(type=PresentationSectionType.NORMAL)
        self.add(Exactas)
        self.wait()

        self.next_section(type=PresentationSectionType.NORMAL)
        self.add(Trianguladas)
        self.wait()

        self.next_section(type=PresentationSectionType.NORMAL)
        self.add(Semisimples)
        self.wait()

        self.next_section(type=PresentationSectionType.NORMAL)
        self.add(Extrianguladas)
        self.wait()
        self.play(Indicate(Extrianguladas, scale_factor=1.1, color=NARANJA))

class Motivacion(MovingCameraScene):

    def construct(self):

        texto1 = Tex(r"""\begin{itemize}
                        \item[$\bullet$] Se conoce una relación entre las categorías exactas y las trianguladas, dada por las categorías de Frobenius y sus categorías estables asociadas[2].
                        \item[$\bullet$] Muchos resultados de naturaleza homológica son válidos tanto en categorías exactas como en categorías trianguladas.
                        \item[$\bullet$] Los procesos de ``adaptación de pruebas'' para transferir resultados entre un tipo de categoría y otra suelen ser difíciles.
                        \end{itemize}
                        """).scale(escalaTexto).align_on_border(LEFT, buff=buffIzquierdo).shift(0.75*UP)
        texto1[0][125].set_color(VERDE)
        texto1[0][128:].set_fill(opacity=0)
        texto2 = Tex(r"\justifying El uso de categorías extrianguladas remueve dificultades encontradas durante este proceso[3]. Su definición se obtuvo axiomatizando las propiedades de los bifuntores $\text{Ext}^1$ relevantes para los pares de cotorsión (completos).").scale(escalaTexto).next_to(texto1, 3*DOWN)
        texto2[0][80].set_color(VERDE)
        texto2[0][:].set_fill(opacity=0)
        textos = Group(texto1, texto2)

        # Primera diapositiva
        self.next_section(type=PresentationSectionType.NORMAL)
        self.add_slide_frame("Motivación", "", 6)
        self.add(textos)
        self.move_camera(ORIGIN)

        self.next_section(type=PresentationSectionType.NORMAL)
        texto1[0][128:231].set_fill(opacity=1)
        self.wait()

        self.next_section(type=PresentationSectionType.NORMAL)
        texto1[0][231:].set_fill(opacity=1)
        self.wait()

        self.next_section(type=PresentationSectionType.NORMAL)
        texto2[0][0:83].set_fill(opacity=1)
        self.wait()

        self.next_section(type=PresentationSectionType.NORMAL)
        texto2[0][83:].set_fill(opacity=1)
        self.wait()
