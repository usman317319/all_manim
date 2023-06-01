from manim import *

config.background_color = WHITE
class Ex1(Scene):
    def construct(self):
        MathTex.set_default(color= BLACK, font_size= 35)
        setA = MathTex(r"A = \{(x,y) \in \mathbb{R}^2 ; y=x , 0 \le x \le 1\}", color= "#0bfc03").to_edge(UL)
        setB = MathTex(r"B = \{(x,y) \in \mathbb{R}^2 ; y=-x , 0 \le x \le 1\}", color= "#2c03fc").next_to(setA, DOWN)
        f = MathTex("f: \mathbb{R}^2 \longrightarrow \mathbb{R} ( a\ projection\ map)").next_to(setB, DOWN)
        f_xy = MathTex("f((x,y)) = x").next_to(f, DOWN)

        axes = Axes(x_range= [-2,2,1], y_range= [-2,2,1], x_length= 5, y_length= 4, tips= False).add_coordinates().set_color(BLACK).to_corner(RIGHT)

        setA_graph = ParametricFunction(lambda t: axes.c2p(t,t), t_range= [0,1], color= "#0bfc03")
        setB_graph = ParametricFunction(lambda t: axes.c2p(t,-t), t_range= [0,1], color= "#2c03fc")

        self.add(setA, setB, axes, f, f_xy, setA_graph, setB_graph)