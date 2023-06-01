from manim import *

class arclength(Scene):
    def construct(self):
        title = Title("Arc Length", font_size= 35, match_underline_width_to_text= True, underline_buff= 0.1)
        self.play(Create(title))
        ang = ValueTracker(0)
        angle = always_redraw(lambda : Arc(
            start_angle= 0,
            angle = ang.get_value(),
            radius= 0.3
        ))
        angle_tex = always_redraw(lambda : MathTex(rf"{round(np.rad2deg(ang.get_value()),2)} ^\circ", font_size= 15).move_to(np.array([0.5,0.2,0])))
        arc1 = always_redraw(lambda : Arc(
            start_angle= 0,
            angle = ang.get_value(),
            radius= 1,
            color= RED
        ))
        radius = Line(start= ORIGIN, end= arc1.get_start())
        moving_radius = always_redraw(lambda : Line(start= ORIGIN, end= arc1.get_end()))

        self.add(arc1, radius, moving_radius, angle, angle_tex)
        self.play(ang.animate.increment_value(PI/4), run_time= 1.5)
        arc1.clear_updaters()
        angle.clear_updaters()
        moving_radius.clear_updaters()
        angle_tex.clear_updaters()
        arc1_copy = arc1.copy()
        arc2 = Arc(
            start_angle= PI/4,
            angle= 7*(PI/4),
            radius= 1,
            color= YELLOW
        )
        self.play(Create(arc2))

        self.wait(1)
        l1 = Line(start= np.array([1,0,0]), end= np.array([1,(PI/4),0]), color= RED)
        l1.rotate(PI/2 - l1.get_angle())
        
        self.add(arc1)
        self.play(arc1.animate.become(l1).shift(RIGHT * 2), run_time= 2)
        numline = NumberLine(length= l1.get_length(), x_range= [0,PI/4,PI/4]).rotate(PI/2).next_to(l1, RIGHT, buff= 2.1)
        length = MathTex(r"{\frac{\pi}{4}}", font_size= 30).next_to(numline, RIGHT)
        self.play(Create(numline))
        self.play(Write(length))
        self.wait(1)
        self.play(Rotate(radius, angle= -PI/2, about_point= radius.get_right()))
        self.play(radius.animate.next_to(numline, LEFT, buff= 0.2))
        times_angle = MathTex(r"\times", font_size= 25).next_to(radius, LEFT)
        self.play(
            Create(times_angle),
            angle_tex.animate.next_to(times_angle, LEFT, buff= 0.1).scale(1.3)
        )
        self.wait(2)
        radius_copy = radius.copy().stretch_to_fit_height(PI/4)
        self.play(
            radius.animate.stretch_to_fit_height(PI/4),
            VGroup(angle_tex, times_angle).animate.become(radius_copy)
        )
        self.wait(3)
        self.play(FadeOut(VGroup(numline, length, radius, angle_tex, times_angle)))
        self.play(arc1.animate.become(arc1_copy), run_time= 2)
        self.wait(2)


class circle_len(arclength):
    def construct(self):
        ang = ValueTracker(0)

        # Building up a NumberLine and labeling the points
        angle = 0
        numline = NumberLine(length= 2*PI, x_range= [0,2*PI, PI/6], unit_size= PI/6).rotate(PI/2).to_edge(LEFT).shift(RIGHT * 0.3)
        rad_scl = Tex("Radian Scale", font_size= 25).next_to(numline, UP, buff= 0.2)
        MathTex.set_default(font_size= 20)
        angles_rad = list(map(MathTex, [
            r"0",
            r"\frac{\pi}{6}",
            r"\frac{\pi}{3}",
            r"\frac{\pi}{2}",
            r"\frac{2\pi}{3}",
            r"\frac{5\pi}{6}",
            r"\pi",
            r"\frac{7\pi}{6}",
            r"\frac{4\pi}{3}",
            r"\frac{3\pi}{2}",
            r"\frac{5\pi}{3}",
            r"\frac{11\pi}{6}",
            r"2\pi",
        ]))
        for i in range(0, len(angles_rad)):
            angles_rad[i].move_to(numline.n2p(PI/6 * i)).shift(RIGHT * 0.5)
        
        # Radians on numberLine
        dot = always_redraw(lambda : Dot(point= numline.n2p(ang.get_value())))
        path = TracedPath(dot.get_center, stroke_color= "#fcba03", stroke_width= 3)

        # Degree Angles
        axes_circle = Axes().shift(LEFT * 3)
        frame = ParametricFunction(lambda t: axes_circle.c2p(np.cos(t), np.sin(t)), t_range= [0,2*PI]).move_to(axes_circle.get_center())
        degree_meter = Tex("Degree Scale").next_to(frame, UP * 2)
        angles = ["0", "30", "45", "60", "90", "120", "135", "150", "180", "210", "225", "240", "270", "300", "315", "330"] 
        angles_deg = list(map(MathTex,
            [
                r"0 ^\circ", "30 ^\circ", "45 ^\circ", "60 ^\circ", "90 ^\circ", "120 ^\circ", "135 ^\circ", "150 ^\circ", "180 ^\circ", "210 ^\circ", "225 ^\circ", "240 ^\circ", "270 ^\circ", "300 ^\circ", "315 ^\circ", "330 ^\circ"
            ]
            ))
        
        lines = list()
        for i in range(len(angles_deg)):
            angle = int(angles[i])
            angles_deg[i].move_to(
                axes_circle.c2p(np.cos(np.deg2rad(angle)), np.sin(np.deg2rad(angle)))
                ).shift( 
                (RIGHT * np.cos(np.deg2rad(angle)) + UP * np.sin(np.deg2rad(angle))) * 0.4
                )
            line = Line(start= [-0.05,0,0], end= [0.05,0,0]).move_to(
                axes_circle.c2p(np.cos(np.deg2rad(angle)), np.sin(np.deg2rad(angle)))
                ).rotate(np.deg2rad(angle))
            lines.append(line)
            self.add(line)
        vec = always_redraw(lambda : Line(start= axes_circle.c2p(0,0), end= axes_circle.c2p(np.cos(ang.get_value() ), np.sin(ang.get_value()) )).add_tip(tip_length= 0.1, tip_width= 0.1))


        self.add(VGroup(*angles_rad), rad_scl, VGroup(*angles_deg), frame, vec, degree_meter)

        # Making circle
        circle = Circle(radius= 1).shift(RIGHT * 4)
        origin = Dot(circle.get_center())
        arc = always_redraw(lambda : Arc(
            start_angle= 0,
            angle = ang.get_value(),
            radius= 1
        ).shift(RIGHT * 4))
        l1 = always_redraw(lambda : Line(start= circle.get_center(), end= arc.get_start()))
        l2 = always_redraw(lambda : Line(start= circle.get_center(), end= arc.get_end()))
        

        self.add(arc, l1, l2, numline, dot, path, origin)
        self.play(ang.animate.increment_value(PI/6), run_time= 10, rate_func= rate_functions.linear)
        arc_len = arc.copy()
        self.wait(2)