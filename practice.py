from manim import *
from numpy import *

class transformations(Scene):
    def construct(self):
        Tex.set_default(font_size= 30)

        title = Title("Types of Linear Transformations", match_underline_width_to_text= True, font_size= 35).shift(UP*0.4)

        # All Text
        conditions = Tex("Conditions for a Transformation to be Linear...").to_corner(LEFT).shift(UP * 2)
        conditions[0][14:28].set_color(YELLOW)
        conditions[0][-4:-10:-1].set_color(YELLOW)
        c1 = Tex("1.All the gird lines should remain").next_to(conditions, DOWN, aligned_edge= LEFT)
        c1p1 = Tex("parallel and evenly spaced.").next_to(c1, DOWN, aligned_edge= LEFT)
        c2 = Tex("2.The ORIGIN must remain at it's position.").next_to(c1p1, DOWN, aligned_edge= LEFT)

        stretching = Tex("1.Stretching axes by some scalar factor.").next_to(c2, DOWN, buff= 1.2)
        rotating = Tex("2.Rotating by some angle.").next_to(stretching, DOWN, aligned_edge= LEFT)
        shear = Tex("3.Applying Shear.").next_to(rotating, DOWN, aligned_edge= LEFT)

        # Axes
        background = NumberPlane(x_range= [-6,6,1],x_length= 6, y_length= 6, background_line_style= {"stroke_opacity": 0.2} ).to_corner(RIGHT)
        foreground = NumberPlane(x_range= [-6,6,1],x_length= 6, y_length= 6).to_corner(RIGHT)

        # Animations and Creating Scenes
        self.play(Create(VGroup(title, background, foreground), run_time= 1))
        self.wait(1)
        self.play(Write(conditions), run_time= 3)
        self.wait(2)
        self.play(Write(VGroup(c1, c1p1)), run_time= 3)
        self.wait(3)
        self.play(Write(c2), run_time= 3)
        self.wait(12)
        self.play(Write(stretching), foreground.animate.scale(0.5), run_time= 2)
        self.play(Write(rotating), Rotate(foreground, angle= -PI), run_time= 2)
        self.play(Write(shear), run_time= 2)
        self.wait(2)

        self.play(FadeOut(VGroup(title, background, foreground, conditions, c1, c1p1, c2, stretching, rotating, shear)))
        self.wait(1)

        # Scene 2
        background = NumberPlane(y_range= [-10, 10],y_length= 20,background_line_style= {"stroke_color": YELLOW, "stroke_width": 0.4})
        foreground = NumberPlane(y_range= [-10, 10],y_length= 20)
        i =  Vector(background.c2p(1,0), color= YELLOW)
        i_label = MathTex(r"\hat{i}", font_size= 35, color= YELLOW).next_to(i, UP)
        j = Vector(background.c2p(0,1), color= RED)
        j_label = MathTex(r"\hat{j}", font_size= 35, color= RED).next_to(j, LEFT)
        e1 = Vector(foreground.c2p(1,0))
        e1_lab = MathTex(r"e_1", font_size= 35).next_to(e1, UP, buff= 0.1)
        e1.add(e1_lab)
        e2 = Vector(foreground.c2p(0,1))
        e2_lab = MathTex(r"e_2", font_size= 35).next_to(e2, LEFT, buff= 0.1)
        e2.add(e2_lab)

        self.play(Create(VGroup(background, i, j, i_label, j_label)), run_time= 2)
        self.wait(11)

        i_s = []
        prei = i.copy()
        prej = j.copy()
        for iter in range(6):
            i_copy = prei.copy()
            j_copy = prej.copy()
            i_s.append(i_copy)
            i_s.append(j_copy)
            self.play(
                Rotate(
                i_copy,
                angle= PI,
                about_point= i_copy.get_right()
                ),
                Rotate(
                j_copy,
                angle= PI,
                about_point= j_copy.get_top()
                ),
                run_time= 1
            )
            prei = i_copy
            prej = j_copy
        self.wait(2)
        self.play(FadeOut(VGroup(*i_s)), run_time= 1)

        es = VGroup(e1, e2)
        rec = BackgroundRectangle(es, color= WHITE)
        rec.scale(1.3)
        es.add(rec)
        es.shift(UP * 2 + RIGHT * 4.2)

        self.wait(3)
        self.play(Create(es[2]), run_time= 2)
        self.wait(1)
        self.play(Create(es[0]))
        self.wait(0.5)
        self.play(Create(es[1]))
        self.wait(8)
        self.play(FadeOut(VGroup(es[2], i_label, j_label)))
        es.remove(rec)
        self.wait(3.5)
        self.play(es.animate.shift(UP * -2 + RIGHT * -4.2))
        self.wait(1)

        e1 = always_redraw(lambda : Vector(foreground.c2p(1,0), color= BLUE))
        e2 = always_redraw(lambda : Vector(foreground.c2p(0,1), color= BLUE))
        self.add(e1, e2)
        self.remove(es)

        m = Matrix([[1,0], [0,1]]).to_edge(UL)
        m.add_background_rectangle()
        m[0].scale(1.1)

        self.wait(6.8)
        self.play(Create(m[0]), Create(m[2]), Create(m[3]))
        self.wait(1)
        self.play(Write(VGroup(m[1][0], m[1][2])), Indicate(e1, color= BLUE), run_time= 3)
        self.wait(0.5)
        self.play(Write(VGroup(m[1][1], m[1][3])), Indicate(e2, color= BLUE), run_time= 3)
        self.wait(1)
        self.play(Create(foreground), run_time= 1)
        self.add(e1, e2)
        
        i_copy = i.copy()
        i_copy_label = always_redraw(lambda : MathTex(r"\hat{i}", font_size= 35, color= BLACK).next_to(i_copy))
        e1_copy = e1.copy()
        e1_copy_label = MathTex(r"e_1", font_size= 35, color= BLACK).next_to(e1_copy)
        vecs = VGroup(i_copy, e1_copy)
        rec_copy = BackgroundRectangle(vecs, color= WHITE).scale(4).shift(UP*2.5 + RIGHT*4)

        self.wait(7)
        self.play(Create(rec_copy), run_time= 0.5)
        self.play(i_copy.animate.shift(UP*2.7 + RIGHT * 3))
        self.play(Write(i_copy_label), run_time= 0.3)
        self.play(e1_copy.animate.next_to(i_copy, DOWN))
        # Using a line instead of vector for stretching
        e1_copy_label = MathTex(r"e_1", font_size= 35, color= BLACK).next_to(e1_copy)
        e1_copy_line = always_redraw(lambda : Line(start= e1_copy.get_left(), end= e1_copy_label.get_left()-[0.25,0,0], stroke_width= e1_copy.get_stroke_width(), color= e1_copy.get_color()).add_tip(tip_length= e1_copy[1].get_length(), tip_width= e1_copy[1].get_width()))
        self.add(e1_copy_line)
        self.remove(e1_copy)
        self.add(e1_copy_label)
        self.wait(1)
        self.play(e1_copy_label.animate.shift(RIGHT * 1))
        self.wait(1)

        MathTex.set_default(font_size= 30)
        # Matrix.set_default(v_buff= 0.4)
        factor = MathTex("2").next_to(rec_copy, DOWN, buff= 0.9).shift(LEFT * 1.5)
        e1_col = Matrix([[1],[0]]).next_to(factor, RIGHT)
        equals_to = MathTex("=").next_to(e1_col, RIGHT)
        e1_col_mul = Matrix([[2],[0]]).next_to(equals_to, RIGHT)
        cals = VGroup(factor, e1_col, equals_to, e1_col_mul)
        cals.add_background_rectangle(color= BLACK)
        cals[0].scale(1.3)

        self.play(Create(cals[0]))
        self.wait(1)
        self.play(Write(VGroup(factor, e1_col)), run_time= 1)
        self.wait(1)
        self.play(Create(equals_to), Write(e1_col_mul), run_time= 1.5)
        self.wait(1)

        self.play(FadeOut(VGroup(factor, e1_col, equals_to)), run_time= 0.3)
        self.play(m[1][0].animate.set_color(BLACK), m[1][2].animate.set_color(BLACK), run_time= 0.1)
        self.play(VGroup(e1_col_mul[0][0], e1_col_mul[0][1]).animate.move_to(VGroup(m[1][0], m[1][2]).get_center()))
        self.play(FadeOut(VGroup(cals[0], e1_col_mul[1], e1_col_mul[2], i_copy, e1_copy_line, i_copy_label, e1_copy_label, rec_copy)), run_time= 0.3)
        self.play(e1_col_mul[0][0].animate.scale(1.5), e1_col_mul[0][1].animate.scale(1.5), run_time= 0.5)
        self.wait(1)
        m[1][0].become(e1_col_mul[0][0])
        m[1][2].become(e1_col_mul[0][1])
        m[1][0].set_color(WHITE)
        m[1][2].set_color(WHITE)
        self.remove(e1_col_mul[0][0],e1_col_mul[0][1])
        self.wait(1)

        # Stretching

        m1 = [[2,0],[0,1]]
        self.wait(4)
        self.play(ApplyMatrix(m1, foreground))
        self.wait(6)

        e1_copy1 = e1.copy()
        brace = Brace(e1, DOWN)
        length = Tex("2").next_to(brace, DOWN)
        self.add(e1_copy1)
        self.play(Rotate(e1_copy1, angle= -PI, about_point= e1_copy1.get_right()), run_time= 2)
        self.wait(5)
        self.play(FadeOut(e1_copy1))
        self.play(Create(brace))
        self.wait(1.3)
        self.play(Write(length))
        self.wait(4)
        self.play(FadeOut(brace, length))
        self.wait(3)

        self.wait(11)
        m2 = [[1,0],[0,1/2]]
        self.play(m[1][3].animate.become(MathTex(r"\frac{1}{2}", font_size= 35).shift(m[1][3].get_center())))
        self.wait(10)
        self.play(ApplyMatrix(m2, foreground))

        self.wait(16)

        m12_inv = [[1/2, 0], [0, 2]]
        self.wait(7)
        self.play(ApplyMatrix(m12_inv, foreground))
        self.wait(1)

        # Rotation
        self.add(foreground)
        m1r = [[0,1],[-1,0]]
        self.play(ApplyMatrix(m1r, foreground))
        self.wait(1)

        m1r_inv = [[0,-1],[1,0]]
        self.play(ApplyMatrix(m1r_inv, foreground))
        self.wait(1)

        m2r = [[0,-1],[1,0]]
        self.play(ApplyMatrix(m2r, foreground))
        self.wait(1)

        m2r_inv = [[0,1],[-1,0]]
        self.play(ApplyMatrix(m2r_inv, foreground))
        self.wait(1)

        m3r = [[-1,0],[0,-1]]
        self.play(ApplyMatrix(m3r, foreground))
        self.wait(1)

        m3r_inv = [[-1,0],[0,-1]]
        self.play(ApplyMatrix(m3r_inv, foreground))
        self.wait(1)

        m4r = [[1/np.sqrt(2), 1/np.sqrt(2)], [-1/np.sqrt(2), 1/np.sqrt(2)]]
        self.play(ApplyMatrix(m4r, foreground))
        self.wait(1)

        m4r_inv = [[1/np.sqrt(2), -1/np.sqrt(2)], [1/np.sqrt(2), 1/np.sqrt(2)]]
        self.play(ApplyMatrix(m4r_inv, foreground))
        self.wait(1)

        m3 = [[1, 0], [1/np.sqrt(2), 1/np.sqrt(2)]]
        self.play(ApplyMatrix(m3, foreground), m[1][3].animate.become(MathTex(r"1", font_size= 35).shift(m[1][3].get_center())), m[1][0].animate.become(Tex("1").shift(m[1][0].get_center())))
        self.wait(1)


        # m4 = [[0,1],[-1,0]]
        # self.play(ApplyMatrix(m4, foreground), m[1][3].animate.become(MathTex(r"1", font_size= 35).shift(m[1][3].get_center())), m[1][0].animate.become(Tex("1").shift(m[1][0].get_center())))
        # self.wait(1)