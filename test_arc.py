from manim import *

class Test(Scene):
    def construct(self):
        title = Title("Arc Length", match_underline_width_to_text= True)

        a1 = Arc(
            start_angle= 0,
            angle= PI/4,
            radius= 1
        )
        a2 = Arc(
            start_angle= PI/4,
            angle= 2*PI,
            radius= 1
        )
        
        