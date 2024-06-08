from manim import *
import random

class video(ThreeDScene):
    def line(self, t):
        return self.axes.c2p(4+3*t, 3-4*t, 5+7*t)

    def construct(self):
         # The main 3d Axes, We use this number system to place all the objects
        self.axes = ThreeDAxes()

        # The Pipe representing the tower
        pipe = Surface(lambda u, v : self.axes.c2p(0.1*np.cos(u), 0.1*np.sin(u), v),
                       u_range= [0, 2*PI], v_range= [0,5],
                       checkerboard_colors= None, fill_color= "#9f02ba"
                      ).shift([4*self.axes.get_x_unit_size(),3*self.axes.get_y_unit_size(),0])
        
        # Dots and Points. Coordinates are given where each needs to go
        pipeDot = Dot().move_to(self.axes.c2p(4,3,0))
        pipeDotText = MathTex("[4,3,0]").next_to(pipeDot, UR)
        pipeTopText = MathTex("[4,3,5]").move_to(self.axes.c2p(4,3,5.5)).rotate(PI/2,axis= [1,0,0]).rotate(3*PI/4, axis= [0,0,1])

        # This is the ground. Equation of a Plane
        plane = Surface(lambda u, v : self.axes.c2p(u,v,0),
                        u_range= [-100, 100], v_range= [-100, 100],
                        checkerboard_colors= None,
                        fill_color= "#45d104"
                       )
        
        # The is the sun. A sphere
        sun = Sphere(radius= 0.5, fill_color= "#fff708", checkerboard_colors= None, resolution= 128).shift(self.line(t= 1))

        # Setting the camera. use https://www.geogebra.org/m/hqPfxIpp this to decide values of phi and theta
        self.set_camera_orientation(phi= 0, theta= -PI/2)


        # Here we show things on the screen. Create creates the thing and wait means to wait for 1 second
        self.play(Create(plane))
        self.wait()
        self.play(Create(self.axes))
        self.wait()
        self.move_camera(zoom= 2)    # Zooming in
        self.move_camera(frame_center= [4,0,0])   # Shifting the camera frame
        self.wait()
        self.move_camera(frame_center= [4,3,0])   # Shifting the camera frame again
        self.wait()
        self.play(Create(pipeDot))
        self.play(Write(pipeDotText))
        self.wait()
        self.move_camera(phi= PI/4)   # Changing camera angle
        self.wait()
        self.move_camera(theta=PI/4)  # Changing camera angle again
        self.wait()
        self.move_camera(frame_center= [4,3,2.5], phi= PI/2, zoom= 0.999)   # Changing camera angle and zooming
        self.wait()
        self.play(Create(pipe))
        self.wait()
        self.play(Create(pipeTopText))
        self.wait()

        # Sun Rays are equations of lines. The starting point for these lines is the center of the sun
        # and the ending point is right left behind and forward of the tower
        # also on the tower 
        rays = VGroup()
        raysLeft = VGroup()
        for t in np.linspace(-0.76,0.68,random.randint(35,40)):
            for n in np.linspace(0,2,random.randint(35,40)):
                raysLeft.add(Line(start= sun.get_center(), end= self.axes.c2p(1+n+3*t, 2+n-4*t,0),
                              stroke_color= YELLOW, stroke_width= 0.1
                             )
                        )
        rays.add(raysLeft)

        raysRight = VGroup()
        for t in np.linspace(-0.76,0.68,random.randint(35,40)):
            for n in np.linspace(0,2,random.randint(35,40)):
                raysRight.add(Line(start= sun.get_center(), end= self.axes.c2p(3.2+n+3*t, 4.2+n-4*t,0),
                              stroke_color= YELLOW, stroke_width= 0.1
                             )
                        )
        rays.add(raysRight)

        raysDOWN = VGroup()
        for t in np.linspace(0.25,0.68,random.randint(10,15)):
            for n in np.linspace(0,0.3,random.randint(10,15)):
                raysDOWN.add(Line(start= sun.get_center(), end= self.axes.c2p(3+n+3*t, 4+n-4*t,0),
                              stroke_color= YELLOW, stroke_width= 0.1
                             )
                        )
        rays.add(raysDOWN)

        raysPipe = VGroup()
        for z in np.linspace(0,5,250):
            n = random.uniform(0,0.3)
            raysPipe.add(Line(start= sun.get_center(), end= self.axes.c2p(3+n+3*0.25, 4+n-4*0.25, z),
                            stroke_color= YELLOW, stroke_width= 0.1
                            )
                    )
        rays.add(raysPipe)

        raysBack = VGroup()
        for t in np.linspace(-0.76,-0.51,random.randint(5,10)):
            for n in np.linspace(0,0.3,random.randint(5,10)):
                raysBack.add(Line(start= sun.get_center(), end= self.axes.c2p(3+n+3*t, 4+n-4*t,0),
                              stroke_color= YELLOW, stroke_width= 0.1
                             )
                        )
        rays.add(raysBack)

        
        self.move_camera(frame_center= sun.get_center())
        self.wait()
        self.play(Create(sun))
        self.wait()
        self.move_camera(frame_center= self.line(t= 0.5), phi= PI/2, theta= PI/4, zoom= 0.5)
        self.wait()
        self.play(Create(rays), run_time= 2)
        self.add(sun)
        self.move_camera(frame_center= self.axes.c2p(4,3,1), phi= PI/4, theta= PI/4)
        self.wait()
        self.begin_ambient_camera_rotation(rate= 1.2)
        self.wait(5)
        self.stop_ambient_camera_rotation()
        self.move_camera(frame_center= self.axes.c2p(4,3,1), phi= 1.35, theta= PI/4, zoom= 1.5)
        self.play(FadeOut(raysRight, raysLeft))
        self.wait()
        # self.stop_ambient_camera_rotation()
        # self.wait(4)


        # This is another axes used to show the vector. This is very small
        axesVector = ThreeDAxes(x_length= 1, y_length= 1, z_length= 1,
                                x_range= [-1,1], y_range= [-1,1], z_range= [-1,1],
                                tips= False,
                               ).shift([0,1 * self.axes.get_y_unit_size() ,1])

        # This is the vector
        vec = Line(axesVector.c2p(0,0,0), axesVector.c2p(3/np.sqrt(74), -4/np.sqrt(74), 7/np.sqrt(74))).add_tip(tip_length= 0.1, tip_width= 0.1)
        vec.rotate(PI/2, axis= [3/np.sqrt(74), -4/np.sqrt(74), 7/np.sqrt(74)])

        self.play(Create(axesVector))
        self.play(Create(vec))
        self.wait()

        # The rectangular Screen
        screen = Rectangle(width= 6, height= 4, stroke_color= BLACK, stroke_width = 8, stroke_opacity = 0, fill_color= WHITE, fill_opacity= 0)
        screen.to_edge(UL)

        # Text to be writeen in the screen
        lineP = ParametricFunction(lambda t : self.axes.c2p(4+3*t, 3-4*t, 5+7*t), t_range= [-5/7,1])
        linePText = Tex("(4+3t, 3-4t, 5+7t)").move_to(self.axes.c2p(4,3,5.5)).rotate(PI/2,axis= [1,0,0]).rotate(3*PI/4, axis= [0,0,1])
        screen = Rectangle(width= 6, height= 4, stroke_color= BLACK, stroke_width = 8, stroke_opacity = 0, fill_color= WHITE, fill_opacity= 0)
        screen.to_edge(UL)
        MathTex.set_default(font_size= 25)
        lineEq = VGroup(MathTex(r"Equation of line parallel to v(3,-4,7) \\ and passing through (4,3,5)", tex_environment= "flushleft"),
                        VGroup(MathTex(r"\vec{s} = \begin{bmatrix} 4 \\ 3 \\ 5 \end{bmatrix} + t \cdot \begin{bmatrix} 3 \\ -4 \\ 7 \end{bmatrix}")).arrange(RIGHT),
                        MathTex(r"\vec{s} = (4+3t, 3-4t, 5+7t)")
                       ).arrange(DOWN).set_opacity(0).set_color(BLACK)
        
        # This line fits the object on to the screen (They become 2d)
        self.add_fixed_in_frame_mobjects(lineEq)
        lineEq.move_to(screen)

        self.add_fixed_in_frame_mobjects(screen)
        self.add_fixed_in_frame_mobjects(lineEq)
        self.play(screen.animate.set_opacity(0.7))
        self.play(screen.animate.set_stroke(opacity= 1), run_time= 0.1)
        self.wait()
        self.play(lineEq.animate.set_opacity(1))
        self.wait()
        self.move_camera(frame_center= self.line(t= 0.5), phi= PI/2, theta= PI/4, zoom= 0.5)
        self.play(FadeOut(pipeTopText))
        self.play(Create(lineP))
        self.wait(2)

        # Just text
        interection = VGroup(MathTex("Intersection\ of\ Line\ and\ Plane\ x_3 = 0"),
                             MathTex("x_3 = 0 :"),
                             MathTex("5+7t = 0"),
                             MathTex("t = -\\frac{5}{7}"),
                             MathTex("At\ t = -\\frac{5}{7}: "),
                             MathTex("(\\frac{13}{7}, \\frac{41}{7}, 0)"),
                            ).arrange(DOWN, aligned_edge= LEFT).set_color(BLACK).move_to(screen)
        interection.set_opacity(0)
        self.add_fixed_in_frame_mobjects(interection)
        self.play(lineEq.animate.set_opacity(0))
        self.play(interection.animate.set_opacity(1))
        self.wait()
        # Setting camera
        self.move_camera(frame_center= self.line(t= -5/7), phi= 1.1, theta= 0, zoom= 1.6)
        self.wait()
        point = Dot().move_to(self.line(t= -5/7))
        pointTex = MathTex("[\\frac{13}{7},\\frac{41}{7},0]").rotate(PI/2, axis= [0,0,1]).next_to(point, UL)
        self.play(Create(point))
        self.play(Write(pointTex))
        self.wait(2)
        self.begin_ambient_camera_rotation()
        self.wait(10)
