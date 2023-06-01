from manim import *

class linear(Scene):
    def construct(self):
        t1 = Tex("How Matrix Transform Space")
        for i in t1[0][3:3+6]:
            i.set_color(YELLOW)
        # self.add(t1)

        m1 = Matrix([[1, 0], [0, 1]]).to_edge(UL)
        m1.add_background_rectangle()

        axes_background = NumberPlane(stroke_width= 0.1, stroke_opacity= 0.1)
        axes_foreground = NumberPlane()
        i = always_redraw(lambda : Vector(axes_foreground.c2p(1,0), color= PINK))
        i_label = Tex("i", color= PINK).next_to(i.get_center(), DOWN)
        def i_labelUpdater(mobj):
            mobj.next_to(i.get_center(), DOWN)
        i_label.add_updater(i_labelUpdater)
        j = always_redraw(lambda : Vector(axes_foreground.c2p(0,1), color= YELLOW))
        j_label = Tex("j", color= YELLOW).next_to(j.get_center(), LEFT)
        def j_labelUpdater(mobj):
            j_label.next_to(j.get_center(), LEFT)
        j_label.add_updater(j_labelUpdater)
        vec = always_redraw(lambda : Vector(axes_foreground.c2p(1,1)))
        self.add(axes_background, axes_foreground, i, j, i_label, j_label, vec, m1)