from manim import *

class dijkstra_algorithm(Scene):
    def construct(self):
        title = Title("Dijkstra Algorithm", match_underline_width_to_text= True)
        # self.add(title)
        dotA = Circle(radius= 0.4).shift(LEFT * 6 + UP * 1.5)
        A = Tex("A").shift(dotA.get_center())
        dotB = Circle(radius= 0.4).next_to(dotA, DOWN, buff= 2)
        B = Tex("B").shift(dotB.get_center())
        dotC = Circle(radius= 0.4).next_to(dotA, RIGHT, buff= 2)
        C = Tex("C").shift(dotC.get_center())
        dotD = Circle(radius= 0.4).next_to(dotB, RIGHT, buff= 2)
        D = Tex("D").shift(dotD.get_center())
        dotE = Circle(radius= 0.4).next_to(dotB, RIGHT, buff= 2)
        dotE = Circle(radius= 0.4).move_to((dotA.get_center() + dotB.get_center()) /2).shift(RIGHT * 5)
        E = Tex("E").shift(dotE.get_center())

        Tex.set_default(font_size= 30)
        AB = Line(dotA.get_bottom(), dotB.get_top())
        lAB = Tex("1").next_to(AB.get_center(), LEFT)
        AC = Line(dotA.get_right(), dotC.get_left())
        lAC = Tex("3").next_to(AC.get_center(), UP)
        BD = Line(dotB.get_right(), dotD.get_left())
        lBD = Tex("4").next_to(BD.get_center(), DOWN)
        CD = Line(dotC.get_bottom(), dotD.get_top())
        lCD = Tex("2").next_to(CD.get_center(), RIGHT)
        CE = Line(dotC.get_right(), dotE.get_left())
        lCE = Tex("1").next_to(CE.get_center(), UP)
        DE = Line(dotD.get_right(), dotE.get_left())
        lDE = Tex("5").next_to(DE.get_center(), DOWN)
        BC = Line(dotB.get_critical_point(UR), dotC.get_critical_point(DL)).scale(1.1)
        lBC = Tex("1").next_to(BC.get_center(), UP)

        graph =  VGroup(dotA, dotB, dotC, dotD, A, B, C, D, dotE, E, AB, AC, BD, CD, CE, DE, lAB, BC, lAC, lBD, lCD, lCE, lDE, lBC)

        # self.add(dotA, dotB, dotC, dotD, A, B, C, D, dotE, E, AB, AC, BD, CD, CE, DE, lAB, BC, lAC, lBD, lCD, lCE, lDE, lBC)
        a = MathTex("")
        # MathTex.set_default(font_size= 20)
        table = MathTable(
            [["Vertex", r"Shortest\ distance\\from A", r"Previous\\Vertex"],
             ["A", r"0", ""],
             ["B", r"2", "D"],
             ["C", r"5", "E"],
             ["D", r"1", "A"],
             ["E", r"1", "D"]],
            include_outer_lines = True
        ).scale(0.4).to_corner(RIGHT)
        table[0][4].set_color(BLACK)

        vertex_visited = Tex("vertex\_visited=[A,B,C,D,E]").next_to(graph, DOWN, buff= 0.7)
        vertex_visited[0][16:len(vertex_visited[0])-1].set_color(BLACK)
        vertex_unvisited = Tex("vertex\_unvisited=[A,B,C,D,E]").next_to(vertex_visited, DOWN, buff= 0.3)

        # self.add(table)

        self.play(Write(title), run_time= 3)
        self.wait(7)
        self.play(Create(table), run_time= 1)
        self.wait(1)
        self.play(Create(graph), run_time= 1)
        self.wait(12)
        self.play(Indicate(VGroup(dotA, A)), run_time= 2)
        self.wait(4)
        self.play(Indicate(VGroup(dotE, E)))
        self.wait(5)
        for i in range(1,5):
            self.play(table[0][4 + i*3].animate.become(MathTex(r"\infty", font_size= 30).shift(table[0][4 + i*3].get_center())))
        for i in range(0,5):
            table[0][5 + i*3].set_color(BLACK)
        self.wait(5)
        self.play(Create(vertex_visited), run_time=2)
        self.wait(1)
        self.play(Create(vertex_unvisited), run_time= 2)
        self.wait(1)
        self.play(Indicate(dotA))
        dotA.set_opacity(0.5)
        self.wait(3)
        # self.play(table[0][4].animate.become(MathTex(r"0", font_size= 20).shift(table[0][4].get_center())))
        table[0][4].set_color(WHITE)
        self.wait(4)
        self.play(Indicate(VGroup(dotB, B, dotC, C)))
        self.wait(1)
        self.play(Indicate(vertex_unvisited[0][20:23]))
        self.wait(1)