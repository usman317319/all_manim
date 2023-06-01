from manim import *

class circle(Scene):
    def construct(self):
        title = Title("Connection between Linear and Circular Motion", match_underline_width_to_text= True, font_size= 30).shift(RIGHT * 3.5)

        # Defining All Axes
        axes_sin = Axes(
            x_range= [0,2*PI,PI/2],
            y_range= [-1,1],
            x_length= 2*PI,
            y_length= 3,
            tips= False
        ).shift(UP*1.8+LEFT*3.7)
        x_pos = [PI/2, PI, 3*PI/2, 2*PI]
        x_vals = ["$\pi$/2", "$\pi$", "3$\pi$/2", "2$\pi$"]
        x_dict = dict(zip(x_pos, x_vals))
        axes_sin.add_coordinates(x_dict)
        
        axes_cos = axes_sin.copy().next_to(axes_sin, DOWN, buff= 1)

        axes_circle = Axes(
            x_range= [-1.5,1.5],
            y_range= [-1.5,1.5],
            x_length= 4,
            y_length= 4,
            tips= False
        ).shift(DOWN * 1.2 + RIGHT * 4)

        # Axes Labels
        sin_label = Tex("sin(x)", color= "#0cf55e").next_to(axes_sin, UP, buff= 0)
        cos_label = Tex("cos(x)", color= "#0c37f5").next_to(axes_cos, UP, buff= 0)
        circle = Tex("Circle").next_to(axes_circle, DOWN)

        # x value
        x = ValueTracker(0)
        
        # Values Lables
        x_label = always_redraw(lambda: Tex(f"x={round(x.get_value(),3)}").next_to(title, DOWN))

        # Putting Values in functions
        sin_dot = always_redraw(lambda : Dot(point= axes_sin.c2p(x.get_value(), np.sin(x.get_value()))))
        # cos_dot = always_redraw(lambda : Dot(point= axes_cos.c2p(x.get_value(), np.cos(x.get_value()))))

        # Pahts
        sin_dot_path = TracedPath(sin_dot.get_center, stroke_color= "#0cf55e")
        # cos_dot_path = TracedPath(cos_dot.get_center, stroke_color= "#0c37f5")

        self.add(axes_sin, axes_cos, sin_label, cos_label, axes_circle, title, circle, x_label, sin_dot, sin_dot_path)
        self.play(x.animate.increment_value(2*PI), run_time= 2, rate_functions= linear)

        reset = Tex("Resetting")
        reset.add_background_rectangle()
        reset[0].scale(30)
        self.play(Write(reset))
        self.play(FadeOut(reset[1]), run_time= 0.4)
        self.play(FadeIn(reset[1]), run_time= 0.4)
        self.play(FadeOut(reset[1]), run_time= 0.4)
        self.play(FadeOut(sin_dot_path), FadeOut(sin_dot), run_time= 0.1)
        x.increment_value(-2*PI)
        self.play(FadeIn(reset[1]), run_time= 0.4)
        self.play(FadeOut(reset), run_time= 0.4)

        # Putting Values in functions
        # sin_dot = always_redraw(lambda : Dot(point= axes_sin.c2p(x.get_value(), np.sin(x.get_value()))))
        cos_dot = always_redraw(lambda : Dot(point= axes_cos.c2p(x.get_value(), np.cos(x.get_value()))))

        # Pahts
        # sin_dot_path = TracedPath(sin_dot.get_center, stroke_color= "#0cf55e")
        cos_dot_path = TracedPath(cos_dot.get_center, stroke_color= "#0c37f5")

        self.add(cos_dot, cos_dot_path)
        self.play(x.animate.increment_value(2*PI), run_time= 2, rate_functions= linear)

        reset = Tex("Resetting")
        reset.add_background_rectangle()
        reset[0].scale(30)
        self.play(Write(reset))
        self.play(FadeOut(reset[1]), run_time= 0.4)
        self.play(FadeIn(reset[1]), run_time= 0.4)
        self.play(FadeOut(reset[1]), run_time= 0.4)
        self.play(FadeOut(cos_dot_path), FadeOut(cos_dot), run_time= 0.1)
        x.increment_value(-2*PI)
        self.play(FadeIn(reset[1]), run_time= 0.4)
        self.play(FadeOut(reset), run_time= 0.4)


        # Putting Values in functions
        sin_dot = always_redraw(lambda : Dot(point= axes_sin.c2p(x.get_value(), np.sin(x.get_value()))))
        cos_dot = always_redraw(lambda : Dot(point= axes_cos.c2p(x.get_value(), np.cos(x.get_value()))))

        # Pahts
        sin_dot_path = TracedPath(sin_dot.get_center, stroke_color= "#0cf55e")
        cos_dot_path = TracedPath(cos_dot.get_center, stroke_color= "#0c37f5")

        self.add(sin_dot, sin_dot_path,cos_dot, cos_dot_path)
        self.play(x.animate.increment_value(2*PI), run_time= 2, rate_function= linear)

        reset = Tex("Resetting")
        reset.add_background_rectangle()
        reset[0].scale(30)
        self.play(Write(reset))
        self.play(FadeOut(reset[1]), run_time= 0.4)
        self.play(FadeIn(reset[1]), run_time= 0.4)
        self.play(FadeOut(reset[1]), run_time= 0.4)
        self.play(FadeOut(VGroup(sin_dot, sin_dot_path,cos_dot, cos_dot_path)), run_time= 0.1)
        x.increment_value(-2*PI)
        self.play(FadeIn(reset[1]), run_time= 0.4)
        self.play(FadeOut(reset), run_time= 0.4)
