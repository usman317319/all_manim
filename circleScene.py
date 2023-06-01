from manim import *

class Circles(Scene):
    def construct(self):
        ### A main axes around which the axes will revolve
        main_axes = Axes()
        rot_axes = Axes().move_to(main_axes.c2p(0,0,0))
        l = always_redraw(lambda : Line(start= main_axes.c2p(0,0), end= rot_axes.c2p(0,0), color= RED, stroke_width= 0.8))

        # Centered Dot
        main_dot = Dot(point= rot_axes.c2p(0,0))
        def main_dotUpdater(mobj):
            main_dot.move_to(rot_axes.c2p(0,0))
        main_dot.add_updater(main_dotUpdater)
        t = ValueTracker(0)

        def rot_axesUpdater(mobj):
            rot_axes.move_to(main_axes.c2p(0, t.get_value()))
        rot_axes.add_updater(rot_axesUpdater)

        self.add( l, main_dot)
        self.play(t.animate.set_value(2), run_time = 2)
        self.wait(1)
        rot_axes.remove_updater(rot_axesUpdater)


        t1 = ValueTracker(0)
        t2 = ValueTracker(0)
        t3 = ValueTracker(0)

        dot1 = Dot(point= rot_axes.c2p(0, 0)).scale(0.3)
        l1 = always_redraw(lambda: Line(rot_axes.get_center(), dot1.get_center(), color= BLUE, stroke_width= 0.8))
        dot2 = Dot(point= rot_axes.c2p(0, 0), color= RED).scale(0.3)
        l2 = always_redraw(lambda: Line(rot_axes.get_center(), dot2.get_center(), color= RED, stroke_width= 0.8))
        dot3 = Dot(point= rot_axes.c2p(0, 0)).scale(0.3)
        l3 = always_redraw(lambda: Line(rot_axes.get_center(), dot3.get_center(), color= YELLOW, stroke_width= 0.8))

        self.add(dot1, dot2, dot3, l1, l2, l3)
        self.wait(1)

        def dot1Updater(mobj):
            dot1.move_to(rot_axes.c2p(t1.get_value(),0))
        dot1.add_updater(dot1Updater)
        
        def dot2Updater(mobj):
            dot2.move_to(rot_axes.c2p(- t2.get_value(), np.sqrt(3) * t2.get_value()))
        dot2.add_updater(dot2Updater)

        def dot3Updater(mobj):
            dot3.move_to(rot_axes.c2p(- t3.get_value(), - np.sqrt(3) * t3.get_value()))
        dot3.add_updater(dot3Updater)

        self.play(
            t1.animate.set_value(1),
            t2.animate.set_value(0.5),
            t3.animate.set_value(0.5)
        )

        dot1.remove_updater(dot1Updater)
        dot2.remove_updater(dot2Updater)
        dot3.remove_updater(dot3Updater)
        
        ### Rotation Scene
        t = ValueTracker(PI/2)
        t1 = ValueTracker(0)
        t2 = ValueTracker(2*PI/3)
        t3 = ValueTracker(4*PI/3)

        t1p = TracedPath(dot1.get_center, color= BLUE)
        t2p = TracedPath(dot2.get_center, color= RED)
        t3p = TracedPath(dot3.get_center, color= YELLOW)
        self.add(t1p, t2p, t3p)

        def rot_axesUpdater(mobj):
            rot_axes.move_to(main_axes.c2p(2*np.cos(t.get_value()), 2*np.sin(t.get_value())))
        rot_axes.add_updater(rot_axesUpdater)

        def dot1Updater(mobj):
            dot1.move_to(rot_axes.c2p(np.cos(t1.get_value()), np.sin(t1.get_value())))
        dot1.add_updater(dot1Updater)

        def dot2Updater(mobj):
            dot2.move_to(rot_axes.c2p(np.cos(t2.get_value()), np.sin(t2.get_value())))
        dot2.add_updater(dot2Updater)

        def dot3Updater(mobj):
            dot3.move_to(rot_axes.c2p(np.cos(t3.get_value()), np.sin(t3.get_value())))
        dot3.add_updater(dot3Updater)

        self.play(
            t.animate.increment_value(2*PI),
            t1.animate.increment_value(2*PI),
            t2.animate.increment_value(2*PI),
            t3.animate.increment_value(2*PI),
            run_time= 10
        )
        self.wait(3)