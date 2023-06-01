from manim import *

config.background_color = WHITE
class real(Scene):
    def construct(self):
        Tex.set_default(color= BLACK)
        MathTex.set_default(color= BLACK)
        Dot.set_default(color= BLACK)

        def custom_Tex(string, **kwargs):
            text = Tex(string, **kwargs)
            text.scale(0.7).set_stroke(BLACK, 0)
            return text
        def custom_MTex(string, **kwargs):
            text = MathTex(string, **kwargs)
            text.scale(0.7)
            return text

        # Scene 1
        title = Title("Monotonically Increasing and Decreasing", match_underline_width_to_text= True, underline_buff= 0.1)
        self.play(Write(title))
        # Monotonically Increasing and Decreasing
        axesi = Axes(
            x_length= 4,
            x_range= [0,4],
            y_length= 4,
            y_range= [0,4],
            tips= False
        ).add_coordinates().shift(LEFT * 4 + DOWN * 1).set_color(BLACK)
        axesd = axesi.copy().shift(RIGHT * 8)
        self.add(axesi, axesd)

        mi = custom_MTex(r"f_n (x) = n").next_to(axesi, UP)
        md = custom_MTex(r"f_n (x) = \frac{1}{n}").next_to(axesd, UP)

        self.play(Create(VGroup(axesi, axesd)), Write(VGroup(mi, md)), run_time= 2)
        self.wait(1)

        dotsi = list()
        dotsd = list()
        i=0
        n_tex = always_redraw(lambda: custom_MTex(f"n={i}").next_to(title, DOWN))
        self.add(n_tex)
        for i in range(1,5):
            doti = Dot(point= axesi.c2p(i,i)).scale(0.7)
            dotd = Dot(point= axesd.c2p(i,1/i)).scale(0.7)
            dotsi.append(doti)
            dotsd.append(dotd)
            self.play(Create(doti), Create(dotd))

        n_inf = custom_MTex("As\ n \longrightarrow \infty").move_to(n_tex.get_center())
        n_tex.clear_updaters()
        self.play(ReplacementTransform(n_tex, n_inf))

        i_tex = custom_MTex("goes\ to\ \infty").next_to(dotsi[len(dotsi)-1], RIGHT)
        d_tex = custom_MTex("goes\ to\ 0").next_to(dotsd[len(dotsd)-1], UP)

        self.play(Write(i_tex), Write(d_tex))

        convergent = custom_Tex("Convergent").rotate(-PI/6).next_to(dotsd[1], UP, buff=0.1)
        divergent = custom_Tex("Divergent").rotate(PI/4).next_to(dotsi[1], UP, buff= 0.1)

        self.play(Write(convergent), Write(divergent))

        self.wait(2)

        self.clear()
        self.wait(0.5)

        # Scene 2
        task1 = custom_MTex(r" \sum_{k=1}^{\infty} (-1)^{(k+1)} (\sqrt[k]{3}-1)").to_edge(UP)

        self.play(Write(task1), run_time= 1.5)
        self.wait(1)
        self.play(Indicate(task1), run_time= 1.5)
        self.wait(1)
        self.play(Indicate(task1[0][5:14]), run_time= 1.5)
        self.wait(1)

        a_k_brace = always_redraw(lambda : Brace(task1[0][14:len(task1[0])], DOWN, buff= 0.1, color= BLACK))
        a_k = always_redraw(lambda : custom_MTex(r"a_k").next_to(a_k_brace, DOWN, buff= 0.1))

        self.play(Create(a_k_brace), Write(a_k))
        self.play(FadeOut(task1[0][0:5]))
        self.play(
            task1[0][5:14].animate.shift(LEFT * 4),
            task1[0][14:len(task1[0])].animate.shift(RIGHT * 3),
        )
        self.wait(1)

        leibniz_criterion = custom_MTex(r"s = \int_{k=1}^{\infty} (-1)^{(k+1)} a_k").to_corner(LEFT)
        leibniz_criterion[0][7:len(leibniz_criterion[0])].set_color(WHITE)
        leibniz_criterion_tex = custom_Tex("Leibniz Criterion").next_to(leibniz_criterion, UP, buff= 0.2)
        leibniz_criterion_rectangle = SurroundingRectangle(leibniz_criterion, color= "#FF0a0a")

        self.play(Write(leibniz_criterion_tex), Create(leibniz_criterion_rectangle), Write(leibniz_criterion))
        self.wait(1)
        
        alter_part = task1[0][5:14].copy()
        ak_part = a_k.copy()
        self.add(alter_part, ak_part)
        self.play(
            alter_part.animate.move_to(leibniz_criterion[0][7:16].get_center()),
            ak_part.animate.move_to(leibniz_criterion[0][16:len(leibniz_criterion[0])].get_center())
        )
        self.wait(1)

        axes_alter = Axes(
            x_range= [0,11,1],
            y_range= [-2,2,1],
            x_length= 6,
            y_length= 4,
            tips= False
        ).add_coordinates().set_color(color= BLACK).shift(RIGHT * 1.5 + DOWN * 1)

        self.play(Create(axes_alter))
        self.wait(1)

        alter_part1 = task1[0][5:14].copy()
        
        self.play(alter_part1.animate.next_to(axes_alter, RIGHT).shift(UP * 2), run_time= 1)
        k_val = 0
        k_tex = always_redraw(lambda : custom_Tex(f"k={k_val}").next_to(alter_part1, UP))
        ans = 1
        alter_part1_ans = always_redraw(lambda : custom_MTex(fr"(-1)^{k_val+1} = {ans}").next_to(alter_part1, DOWN))
        self.play(Create(k_tex))
        self.wait(1)
        self.play(Write(alter_part1_ans))
        all_dots = list()
        for i in range(11):
            k_val = k_val + 1
            ans = (-1)**(k_val+1)
            dot = Dot(point= axes_alter.c2p(k_val, ans)).scale(0.7)
            all_dots.append(dot)
            self.play(Create(dot), run_time= 1)

        alternate = custom_Tex("Alternating")
        for i in range(len(all_dots)):
            self.play(all_dots[i].animate.become(alternate[0][i]))
        sequence = custom_Tex("Sequence").next_to(alternate, RIGHT)
        self.play(Write(sequence))
        alternating_sequence = VGroup(VGroup(*all_dots), sequence)
        self.play(alternating_sequence.animate.next_to(task1[0][5:14], DOWN), run_time= 2)
        self.wait(1)

        axes_conver = Axes(
            x_range= [0,11],
            x_length= 6,
            y_range= [0,5],
            y_length= 5,
            tips= False
        ).add_coordinates().set_color(color= BLACK).shift(RIGHT * 1.5)

        self.play(axes_alter.animate.become(axes_conver))
        self.wait(1)

        k_val = 1
        ans = 0
        self.play(FadeOut(alter_part1), FadeOut(alter_part1_ans))
        conver_part = task1[0][15:19].copy().next_to(k_tex, DOWN)
        conver_part_ans = always_redraw(lambda : custom_MTex(fr"\sqrt[{k_val}]3  = {round(ans,2)}").next_to(conver_part, DOWN))

        self.play(Write(VGroup(conver_part, conver_part_ans)))
        self.wait(1)

        all_dots = list()
        for i in range(11):   
            ans = 3**(1/k_val)
            dot = Dot(point= axes_conver.c2p(k_val, ans)).scale(0.7)
            all_dots.append(dot)            
            self.play(Create(all_dots[i]), run_time= 0.5)
            k_val = k_val + 1
        l_at_1 = ParametricFunction(lambda t: axes_conver.c2p(t,1), t_range= [0,11]).set_color(color= BLACK)
        self.play(Create(l_at_1))
        self.wait(3)

        self.play(FadeOut(VGroup(*all_dots)), FadeOut(l_at_1))
        self.wait(1)

        conver_part1 = task1[0][15:len(task1[0])-1].copy().next_to(k_tex, DOWN)
        conver_part_ans1 = always_redraw(lambda : custom_MTex(fr"\sqrt[{k_val}]3 - 1 = {round(ans,2)}").next_to(conver_part1, DOWN))

        self.play(FadeOut(conver_part_ans), run_time= 0.5)
        self.play(
            conver_part.animate.become(conver_part1),
            Write(conver_part_ans1),
            run_time= 2
        )

        k_val = 1
        ans= 1
        all_dots = list()
        for i in range(11):   
            ans = 3**(1/k_val) - 1
            dot = Dot(point= axes_conver.c2p(k_val, ans)).scale(0.7)
            all_dots.append(dot)            
            self.play(Create(all_dots[i]), run_time= 0.5)
            k_val = k_val + 1
        l_at_0 = ParametricFunction(lambda t: axes_conver.c2p(t,0), t_range= [0,11], color= BLUE)
        self.play(Create(l_at_0))
        self.wait(1)
        self.play(FadeOut(VGroup(conver_part, conver_part_ans1, k_tex)))

        convergent = custom_Tex("Convergent")
        for i in range(10):
            self.play(
                all_dots[i].animate.become(convergent[0][i])
            )
        sequence = custom_Tex("Sequence").next_to(convergent, RIGHT)
        convergent_sequence = VGroup(VGroup(*all_dots), sequence)

        self.play(Write(sequence))
        self.play(convergent_sequence.animate.next_to(a_k, DOWN), run_time= 1)
        self.wait(1)