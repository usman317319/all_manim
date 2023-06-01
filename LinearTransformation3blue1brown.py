from manim import *

class DescribeTransformation(Scene):
    def construct(self):
        self.add_title()
        self.show_function()

    def add_title(self):
        title = Tex("Linear transformation")
        title.to_edge(UP)
        # linear, transformation = title.split()
        brace = Brace(title[0][0:6], DOWN)
        function = Tex("function").next_to(brace, DOWN)
        function.set_color(YELLOW)

        self.play(Write(title))
        self.wait()
        self.play(
            GrowFromCenter(brace),
            Write(function),
            
        )

    def show_function(self):
        f_of_x = Tex("f(x)")
        L_of_v = Tex("L(v)")
        nums = [5, 2, -3]
        num_inputs = VGroup(*list(map(Tex, list(map(str, nums)))))
        num_outputs = VGroup(*[
            Tex(str(num**2))
            for num in nums
        ])
        for mob in num_inputs, num_outputs:
            mob.arrange(DOWN, buff = 1)
        num_inputs.next_to(f_of_x, LEFT, buff = 1)
        num_outputs.next_to(f_of_x, RIGHT, buff = 1)
        f_point = VectorizedPoint(f_of_x.get_center())

        input_vect = Matrix([[5, 7]])
        input_vect.next_to(L_of_v, LEFT, buff = 1)
        output_vect = Matrix([[2, -3]])
        output_vect.next_to(L_of_v, RIGHT, buff = 1)

        vector_input_words = Tex("Vector input")
        vector_input_words.set_color(MAROON_C)
        vector_input_words.next_to(input_vect, DOWN)
        vector_output_words = Tex("Vector output")
        vector_output_words.set_color(BLUE)
        vector_output_words.next_to(output_vect, DOWN)

        self.play(Write(f_of_x, run_time = 1))
        self.play(Write(num_inputs, run_time = 2))
        self.wait()
        for mob in f_point, num_outputs:
            self.play(Transform(
                num_inputs, mob,
                lag_ratio = 0.5
            ))
        self.wait()

        self.play(
            FadeOut(num_inputs),
            Transform(f_of_x, L_of_v)
        )
        self.play(
            Write(input_vect),
            Write(vector_input_words)
        )
        self.wait()
        for mob in f_point, output_vect:
            self.play(Transform(
                input_vect, mob,
                lag_ratio = 0.5
            ))
        self.play(Write(vector_output_words))
        self.wait()        