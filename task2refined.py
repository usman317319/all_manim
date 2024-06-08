from manim import *
import random

class Task2(ThreeDScene):
    def shadowLine(self, t):  # Shadow Line
        return self.axes.c2p(9-3*t, 4+4*t, 0)

    def endShadowLine(self, t):  # Sun Ray that touches the top of tower
        return self.axes.c2p(6+3*t, 8-4*t, 10-t*10)

    def construct(self):
        # The main Axes
        self.axes = ThreeDAxes(x_range= [-10,10], x_length= 13,
                               y_range= [-10,10],
                               z_range= [0,10]
                              ).add_coordinates()
        
        # The Tower (A cylinder)
        pipe = Surface(lambda u, v : self.axes.c2p(0.1*np.cos(u), 0.1*np.sin(u), v),
                       u_range= [0, 2*PI], v_range= [0,10],
                       checkerboard_colors= None, fill_color= "#9f02ba"
                      ).shift([6*self.axes.get_x_unit_size(),8*self.axes.get_y_unit_size(),0])
        
        # Dots, and Texts put on their positions
        shadowStart = Dot().scale(0.7).move_to(self.axes.c2p(6,8,0))
        shadowStartText = MathTex("[6,8,0]").next_to(shadowStart, UP)
        shadowEnd   = Dot().scale(0.7).move_to(self.axes.c2p(9,4,0))
        shadowEndText = MathTex("[9,4,0]").next_to(shadowEnd, RIGHT)
        linebtw = Line(start= shadowStart.get_center(), end= shadowEnd.get_center())
        questionMark = MathTex("?").scale(1.5).move_to(self.axes.c2p(7,5.5,0))

        # Sun
        # The Sun
        sun = Sphere(radius= 0.5, fill_color= "#fff708", checkerboard_colors= None).shift(self.endShadowLine(t= -0.7))
        ray = ParametricFunction(lambda t : self.axes.c2p(6+3*t, 8-4*t, 10-10*t), t_range= [-1,1]) # passes from sun and the top of tower

        # All sun rays starting from center of the sun to around the tower
        rays = VGroup()
        raysPipe = VGroup()
        for z in np.linspace(0,10,250):
            n = random.uniform(-0.1,0.1)
            raysPipe.add(Line(start= sun.get_center(), end= self.axes.c2p(6+n, 8-n, z),
                            stroke_color= YELLOW, stroke_width= 0.1
                            )
                    )
        rays.add(raysPipe)

        raysLeft = VGroup()
        for t in np.linspace(-0.76,1.3,random.randint(35,40)):
            for n in np.linspace(0.15,2.3,random.randint(35,40)):
                raysLeft.add(Line(start= sun.get_center(), end= self.axes.c2p(6+n+3*t, 8+n-4*t,0),
                              stroke_color= YELLOW, stroke_width= 0.1
                             )
                        )
        rays.add(raysLeft)

        raysRight = VGroup()
        for t in np.linspace(-0.76,1.3,random.randint(35,40)):
            for n in np.linspace(-2.3,-0.35,random.randint(35,40)):
                raysRight.add(Line(start= sun.get_center(), end= self.axes.c2p(6.2+n+3*t, 8.2+n-4*t,0),
                              stroke_color= YELLOW, stroke_width= 0.1
                             )
                        )
        rays.add(raysRight)

        raysDOWN = VGroup()
        for t in np.linspace(-0.76, 0,random.randint(35,40)):
            for n in np.linspace(-0.35, 0.15,random.randint(35,40)):
                raysDOWN.add(Line(start= sun.get_center(), end= self.axes.c2p(6.2+n+3*t, 8.2+n-4*t,0),
                              stroke_color= YELLOW, stroke_width= 0.1
                             )
                        )
        rays.add(raysDOWN)

        raysUp = VGroup()
        for t in np.linspace(1, 1.5,random.randint(5,10)):
            for n in np.linspace(-0.35, 0.15,random.randint(35,40)):
                raysUp.add(Line(start= sun.get_center(), end= self.axes.c2p(6.2+n+3*t, 8.2+n-4*t,0),
                              stroke_color= YELLOW, stroke_width= 0.1
                             )
                        )
        rays.add(raysUp)

        self.set_camera_orientation(phi= PI/4, theta= PI/4, zoom= 0.6) # Setting camera 
        self.play(Create(self.axes))
        self.wait()
        self.play(Create(pipe))
        self.wait()
        self.move_camera(phi= PI/2)
        self.wait()
        self.move_camera(frame_center= self.axes.c2p(0,0,10))
        self.wait()
        self.move_camera(frame_center= self.endShadowLine(t= -0.7))
        self.wait()
        self.play(Create(sun))
        self.wait()
        self.move_camera(frame_center= self.axes.c2p(6,8,8))
        self.wait()
        self.play(Create(rays))
        self.wait()
        self.move_camera(frame_center= self.axes.c2p(6,8,0), phi= 0)
        self.wait()
        self.play(Create(linebtw))
        self.wait()
        self.play(FadeOut(raysUp))
        self.wait()
        self.move_camera(phi= 0, theta= -PI/2, frame_center= self.axes.c2p(7.5,6,0), zoom= 1.5)
        self.wait()
        self.play(FadeOut(rays))
        self.wait()
        self.play(Write(questionMark))
        self.wait()

        lineX = DashedLine(self.axes.c2p(9,4,0), self.axes.c2p(6,4,0))
        lineXText = MathTex("x_2 - x_1", font_size= 30).next_to(lineX, DOWN)
        lineXTextAfter = MathTex("9 - 6 = 3", font_size= 30).next_to(lineX, DOWN)
        lineY = DashedLine(self.axes.c2p(6,8,0), self.axes.c2p(6,4,0))
        lineYText = MathTex("y_2 - y_1", font_size= 30).rotate(PI/2).next_to(lineY, LEFT)
        lineYTextAfter = MathTex("8 - 4 = 4", font_size= 30).rotate(PI/2).next_to(lineY, LEFT)
        distance = MathTex(r"\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}", font_size= 20).rotate(-0.83).next_to(linebtw, UR, buff= -1.7)
        distanceAfter = MathTex(r"\sqrt{(3)^2 + (4)^2} = 5", font_size= 20).rotate(-0.83).next_to(linebtw, UR, buff= -1.45)

        self.play(Create(lineX))
        self.play(Create(lineY))
        self.wait()
        self.play(Write(lineXText))
        self.play(Write(lineYText))
        self.wait()
        self.play(Write(distance))
        self.wait()
        self.play(ReplacementTransform(lineXText, lineXTextAfter))
        self.wait()
        self.play(ReplacementTransform(lineYText, lineYTextAfter))
        self.wait()
        self.play(ReplacementTransform(distance, distanceAfter))
        self.wait()
        self.play(FadeOut(lineX, lineY, lineXTextAfter, lineYTextAfter, questionMark, distanceAfter))
        self.wait()

        endShadowLine = ParametricFunction(lambda t : self.endShadowLine(t), t_range= [-5,1])

        self.move_camera(phi= 1.4, theta= 0.64, frame_center= self.axes.c2p(9,4,0))
        self.wait()
        self.play(Create(VGroup(endShadowLine, raysUp[5:], raysDOWN, raysPipe)))
        self.wait()
        
        # Angle
        angle = ArcBetweenPoints(start= self.endShadowLine(0.95),
                                 end= self.shadowLine(0.1),
                                )

        base = MathTex("5").rotate(PI/2, axis= [1,0,0]).rotate(PI/2+self.camera.theta_tracker.get_value(), axis= [0,0,1]).move_to(linebtw).shift([0,0,0.3])
        oppositeSide = Line(self.axes.c2p(6,8,0), self.axes.c2p(6,8,10))
        opp = MathTex("10").rotate(PI/2, axis= [1,0,0]).rotate(PI/2+self.camera.theta_tracker.get_value(), axis= [0,0,1]).move_to(oppositeSide).move_to((self.axes.c2p(5.4,8.8,5)))
        hypotenous = MathTex("\\sqrt{5^2 + 10^2} = 5\\sqrt{5}", font_size= 30).set_opacity(0)
        self.add_fixed_in_frame_mobjects(hypotenous)
        hypotenous.to_corner(LEFT)
        hypo = MathTex(r"5\sqrt{5}").rotate(PI/2, axis= [1,0,0]).rotate(PI/2+self.camera.theta_tracker.get_value(), axis= [0,0,1]).move_to(self.axes.c2p(8.7,4.4,5))
        self.play(Create(angle))
        self.wait()
        self.play(Create(base))
        self.wait()
        self.move_camera(frame_center= self.axes.c2p(7.5,6,5))
        self.wait()
        self.wait()
        self.play(Write(opp))
        self.wait()
        self.move_camera(zoom= 0.8)
        self.wait()
        self.play(hypotenous.animate.set_opacity(1))
        self.wait()
        self.play(Write(hypo))
        self.wait()

        MathTex.set_default(font_size= 30)
        angle = VGroup(MathTex(r"sin(\theta)    = \frac{10}{5\sqrt{5}}"),
                       MathTex(r"\theta = sin^{-1}\left(\frac{10}{5\sqrt{5}}\right)"),
                       MathTex(r"\theta = 63.43^\circ")
                      ).arrange(DOWN, aligned_edge= LEFT).set_opacity(0)
        self.add_fixed_in_frame_mobjects(angle)
        angle.next_to(hypotenous, DOWN)

        angleTex = MathTex("63.43^\\circ").rotate(PI/2, axis= [1,0,0]).rotate(PI/2+self.camera.theta_tracker.get_value(), axis= [0,0,1]).move_to(self.axes.c2p(8.25,5,0.5))

        self.play(angle.animate.set_opacity(1))
        self.wait()
        self.play(Write(angleTex))
        self.wait()