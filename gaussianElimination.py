from manim import *

class elimTrans(Scene):
    def construct(self):
        foreground = NumberPlane(
            x_range= [-5,5,1],
            y_range= [-5,5,1],
            x_length= 6,
            y_length= 6
        )
        background = foreground.copy()
        foreground.apply_matrix([[1,3], [-2,0]])
        foreground.shift(RIGHT * 3)
        background.move_to(foreground.get_center())

        self.add(foreground, background)

