from manim import *
import numpy as np


class System_of_eqations(Scene):
    def construct(self):
        #Объявляю вспомогательные переменные
        scale_for_t1 = 0.4

        z = Text("Решение системы уравнений способом подстановки", font="CMU Serif",font_size=24, gradient=(BLUE, BLUE_A, BLUE))
        z.to_corner(UP)
        # z1 = MathTex('\\begin{cases}x+y=9, \\\\ y^{2}+x = 29. \end{cases}'
        #              ).scale(0.6).next_to(z, DOWN*0.5) #, aligned_edge=LEFT

        z1 = MathTex('x+y=9,'
                     ).scale(0.6).next_to(z, DOWN*0.5) #, aligned_edge=LEFT

        z2 = MathTex('y^{2}+x = 29.'
                     ).scale(0.6).next_to(z1, DOWN*0.5, aligned_edge=LEFT) #

        # https://docs.manim.community/en/stable/reference/manim.mobject.svg.brace.BraceBetweenPoints.html
        # прикрутить эту фигурную скобку к тексту
        # p1 = [0, 0, 0]
        # p2 = [1, 2, 0]
        # brace = BraceBetweenPoints(p1, p2)
        # self.play(Create(NumberPlane()))
        # self.play(Create(brace))
        # self.wait(2)

        a1 = Text("Выберем переменную",font='CMU Serif')
        a2 = Text("Выразим x",font='CMU Serif')
        a3 = Text("Подставим выражение во второе уравнение",font='CMU Serif')
        a4 = Text("Решим второе уравнение",font='CMU Serif')
        a42 = Text('      Найдём корни',font = 'CMU Serif')
        a43 = Text('      Подставим значения в выражения для x',font = 'CMU Serif')
        a5 = Text("Запишем ответ",font='CMU Serif')

        t = VGroup(a1, a2, a3, a4, a42, a43, a5).scale(0.3).set_color(GRAY).arrange(DOWN, center=False, aligned_edge=LEFT).to_corner(
            UL, buff=1.5).shift(DOWN*1.3)

        tr = Triangle(fill_color=WHITE, fill_opacity=1, stroke_color=WHITE).scale(0.1).rotate(PI / 6).next_to(t[0],
                                                                                                              LEFT,
                                                                                                              buff=0.1)
        t1 = Text('Легче выразить переменную x из первого уравнения',font='CMU Serif').scale(scale_for_t1-0.1).next_to(t[0], RIGHT * 10)
        #t1 = Tex('Легче выразить переменную x из первого уравнения',tex_template=TexTemplateLibrary.ctex).scale(scale_for_t1-0.1).next_to(t[0], RIGHT * 10)
        t2 = MathTex(
            "x",  # 0
            "=",  # 1
            "9",  # 2
            "-",  # 3
            "y",  # 4
            ",\\phantom{l}",  # 5
        ).scale(scale_for_t1).next_to(t1, DOWN * 0.9, aligned_edge=LEFT).shift(RIGHT)

        t3=MathTex(
            "y^2",  # 0
            "+",    # 1
            "(9-y)",  # 2
            "=",  # 3
            "29",  # 4
            ";\\phantom{l}",  # 5
        # ).scale(scale_for_t1).next_to(t2, DOWN, aligned_edge=LEFT)
        ).scale(scale_for_t1).next_to(t[2], RIGHT * 2).shift(RIGHT)

        t4 = MathTex(
            """
            y^2+9-y-29 = 0, \ \ \ y^2-y-20 = 0, \ \ \ D=(-1)^2-4\cdot1\cdot(-20) = 81=9^2
            """
         ).scale(scale_for_t1).next_to(t3, DOWN * 0.9, aligned_edge=LEFT).shift(LEFT)
        #).scale(0.4).next_to(t[3],RIGHT*10)

        t5 = MathTex(
            """
            y_1 = \dfrac{1+9}{2} =5 \ \ \ \ \  y_2 = \dfrac{1-9}{2} = -4
            """
        ).scale(scale_for_t1).next_to(t4, DOWN * 0.9, aligned_edge=LEFT)

        t6 = MathTex(
            """
            x_1 = 9-5 = 4 \ \ \ \ \  x_2 = 9-(-4) = 9+4 = 13
            """
        ).scale(scale_for_t1).next_to(t5, DOWN * 0.9, aligned_edge=LEFT)

        t7 = MathTex(
            """
            (4; 5) \ \ \ \ \ (13; -4)
            """
        ).scale(scale_for_t1).next_to(t6, DOWN * 0.9, aligned_edge=LEFT)

        l = Line(UP*3, DOWN * 1, color=GRAY, stroke_width=1).next_to(t, RIGHT).shift(DOWN * 0.1)
        p1=z1.get_corner(UP+LEFT)+[0.15,0,0]
        p2=z2.get_corner(DOWN+LEFT)+[0.15,0,0]
        brace1 = BraceBetweenPoints(p1,p2,sharpness=1.5)


        # Область анимации
        self.play(Write(z))
        self.add(z1)
        self.add(z2)
        self.add(brace1)

        self.play(FadeIn(t, shift=RIGHT))
        self.play(Write(l))
        self.wait()

        self.play(
            Write(tr),
            t[0].animate.set_color(WHITE)
        )

        self.play(
            Write(t1)
        )

        self.play(
            t[0].animate.set_color(GRAY),
            tr.animate.next_to(t[1], LEFT, buff=0.1),
            t[1].animate.set_color(WHITE)
        )


        self.play(Indicate(z1[0][0]))
        self.play(ReplacementTransform(z1[0][0].copy(), t2[0]))
        self.play(Indicate(z1[0][3]))
        self.play(ReplacementTransform(z1[0][3].copy(), t2[1]))
        self.play(Indicate(z1[0][4]))
        self.play(ReplacementTransform(z1[0][4].copy(), t2[2]))
        self.play(Indicate(z1[0][1:3]))
        self.play(ReplacementTransform(z1[0][1:3].copy(), t2[3:6]))
        self.wait()

        self.play(
            t[1].animate.set_color(GRAY),
            tr.animate.next_to(t[2], LEFT, buff=0.1),
            t[2].animate.set_color(WHITE)
        )

        self.play(Indicate(z2[0][0:3]))
        self.play(ReplacementTransform(z2[0][0:3].copy(), t3[0:2]))
        self.play(Indicate(z2[0][3]))
        self.play(ReplacementTransform(z2[0][3].copy(), t3[2]))
        self.play(Indicate(z2[0][4:8]))
        self.play(ReplacementTransform(z2[0][3:8].copy(), t3[3:7]))

        p1=t2.get_corner(UP+LEFT)+[0.15,0,0]
        p2=t3.get_corner(DOWN+LEFT)+[0.15,0,0]
        brace2 = BraceBetweenPoints(p1,p2,sharpness=1.5)
        self.add(brace2)
        self.wait()

        self.play(
            t[2].animate.set_color(GRAY),
            tr.animate.next_to(t[3], LEFT, buff=0.1),
            t[3].animate.set_color(WHITE)
        )
        self.play(Write(t4))
        self.wait()

        self.play(
            t[3].animate.set_color(GRAY),
            tr.animate.next_to(t[4], LEFT, buff=0.1),
            t[4].animate.set_color(WHITE)
        )
        self.play(Write(t5))
        self.play(
            t[4].animate.set_color(GRAY),
            tr.animate.next_to(t[5], LEFT, buff=0.1),
            t[5].animate.set_color(WHITE)
        )
        self.play(Write(t6))
        self.wait()
        self.play(
            t[5].animate.set_color(GRAY),
            tr.animate.next_to(t[6], LEFT, buff=0.1),
            t[6].animate.set_color(WHITE)
        )
        self.play(Write(t7))
        self.wait()

