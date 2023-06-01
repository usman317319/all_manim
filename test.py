from manim import *

class bayes(Scene):
    def construct(self):
        
        """
        # Adding Text like title and virus detection
        medical_test = Title("Medical Test", match_underline_width_to_text= True).to_edge(UL)
        virus_detected = Tex(f"Virus\n\nDetected", font_size= 40)
        for i in range(5,13):
            virus_detected[0][i].set_color(ORANGE)
        virus_detected.add_background_rectangle(color= GREEN, opacity= 0.5)
        virus_detected[0].scale(1.3)
        rectangle = Rectangle(height= virus_detected[0].get_height(), width= virus_detected[0].get_width())
        virus_detected.add(rectangle)
        virus_detected.next_to(medical_test, DOWN, buff= 1)
        self.play(Write(medical_test), run_time= 1.5)
        self.wait(1)
        self.play(Write(virus_detected))
        self.add(virus_detected, virus_detected, rectangle, medical_test)

        # Animation (Moving virus detection box away)
        self.play(virus_detected.animate.to_edge(DR), run_time= 2)


        # Adding people and doing some shifting
        dots = list()
        pre = Dot(fill_opacity= 0.8).scale(1.5).to_edge(UL).shift(DOWN * 1.5)
        dots.append(pre)
        for i in range(1,70):
            d = pre.copy()
            dots.append(d)
            if i%7 ==0:
                d.next_to(dots[i-7], DOWN)
            else:
                d.next_to(pre, RIGHT)
            pre = d
        self.add(VGroup(*dots))

        # Adding signs and colors in 
        a = SVGMobject("test.svg")#.scale(0.3)
        self.play(Create(a))
        self.play(a.animate.scale(0.3))

        pos = [4, 10, 26, 31, 40, 17, 53, 61, 68, 75, 77]
        for i in range(0,len(dots)):
            self.play(a.animate.move_to(dots[i]), run_time= 0.2)
            if i in pos:
                plus = Tex("+", font_size= 35).shift(dots[i].get_center())
                dots[i].set_color(ORANGE)
                dots[i].add(plus)
                
            else:
                negative = Tex("-", font_size= 40).shift(dots[i].get_center())
                dots[i].set_color(GREEN)
                dots[i].add(negative)
        self.play(FadeOut(a))                

        self.play(virus_detected.animate.move_to(ORIGIN))

        tested_truely = Rectangle(height= 2.5, width= 4, fill_color= GREEN, fill_opacity= 0.3).next_to(RIGHT * 2.5 + UP * 1.8)
        t = Tex("Tested Truely").next_to(tested_truely, UP)
        tested_truely.add(t)
        tested_falsely = Rectangle(height= 2.5, width= 4, fill_color= ORANGE, fill_opacity= 0.3).next_to(tested_truely, DOWN, buff= 1.3)
        t = Tex("Tested Falsely").next_to(tested_falsely, UP)
        tested_falsely.add(t)
        self.add(tested_truely, tested_falsely)



        pre = dots[0]
        n = 0
        self.play(pre.animate.scale(0.8).move_to(tested_truely.get_left()).shift(UP * 0.65 + RIGHT * 0.2), run_time= 0.1)
        for i in range(1,int(len(dots)/2) + 3):
            if i%13 != 0:
                self.play(dots[i].animate.scale(0.8).next_to(pre, RIGHT, buff= 0.1), run_time= 0.1)
            elif i%13 == 0:
                self.play(dots[i].animate.scale(0.8).next_to(dots[i-13], DOWN, buff= 0.2), run_time= 0.1)
            pre = dots[i]
            n = i

        self.play(dots[n+1].animate.scale(0.8).move_to(tested_falsely.get_left()).shift(UP * 0.65 + RIGHT * 0.2), run_time= 0.5)

        for i in range(n+2, len(dots)):
            if i%13 != 0:
                self.play(dots[i].animate.scale(0.8).next_to(pre, RIGHT, buff= 0.1), run_time= 0.1)
            elif i%13 == 0:
                self.play(dots[i].animate.scale(0.8).next_to(dots[i-13], DOWN, buff= 0.2), run_time= 0.1)
            pre = dots[i]
            n = i

        ques = Tex(f"If you test positive\n\nfor the test what\n\nis the probability that\n\nyou have the disease?\n\n").shift(LEFT * 4)
        ans = Tex(f"Well a common answer\n\nmay be 99\% because\n\nthe accuracy of the\n\ntest is 99\%.", color= GREEN).next_to(ques, DOWN)
        # self.add(ques, ans)
        self.wait(2)
        self.play(Write(ques), run_time= 3)
        self.wait(1)
        self.play(Write(ans), run_time= 3)
        self.wait(1)


        self.play(FadeOut(
            VGroup(VGroup(*dots), ques, ans, tested_truely, tested_falsely, virus_detected, medical_test)
        ))
        self.wait(1)
        
        
        # Main start
        bayes_theorm = Title("Bayes Theorem", match_underline_width_to_text= True).to_edge(UP)
        # self.add(bayes_theorm)
        self.play(Write(bayes_theorm))
        self.wait(2)

        formula = MathTex(r"P(H|E) = \frac{P(E|H)\times P(H)}{P(E)}").shift(DOWN * 0.3)
        formula[0][2].set_color(GREEN)
        formula[0][4].set_color(ORANGE)
        formula[0][9].set_color(ORANGE)
        formula[0][11].set_color(GREEN)
        formula[0][16].set_color(GREEN)
        formula[0][21].set_color(ORANGE)
        # self.add(formula)
        for i in range(0,3):
            self.play(Write(formula[0][i]), run_time= 0.3)

        act_have = Tex("actually have\n\nthe disease", color= GREEN).next_to(formula[0][0].get_center(), UP * 6)
        arr = Arrow(start= act_have[0][13].get_bottom(), end= formula[0][2].get_top(), color= GREEN)
        given = Tex("given").next_to(act_have[0][20], DOWN, buff= 0.1)

        self.play(Write(act_have), Create(arr), run_time= 0.8)
        self.wait(1.5)
        self.play(Write(given))

        tested_pos = Tex("you tested +", color= ORANGE).next_to(formula[0][3].get_center(), DOWN * 7)
        arr1 = Arrow(start= tested_pos[0][3].get_top(), end= formula[0][4].get_bottom(), color= ORANGE)

        for i in range(3,6):
            self.play(Write(formula[0][i]), run_time= 0.3)
        self.play(Write(tested_pos), Create(arr1))
        self.wait(2)
        self.play(FadeOut(VGroup(act_have, arr, given, tested_pos, arr1)))

        prior_prob = Tex("PRIOR probability of\n\nhaving\n\nthe disease").next_to(formula[0][-7], UP  * 7)
        for i in range(18,len(prior_prob[0])):
            prior_prob[0][i].set_color(GREEN)
        arr2 = Arrow(start= prior_prob.get_bottom(), end= formula[0][-7].get_top(), color= GREEN)

        self.play(Write(formula[0][6]), run_time= 0.3)
        for i in range(14,18):
            self.play(Write(formula[0][i]))
        self.play(bayes_theorm.animate.shift(LEFT * 5))
        self.play(Write(prior_prob), Create(arr2))
        self.wait(2)
        self.play(FadeOut(VGroup(prior_prob, arr2)))
        self.play(bayes_theorm.animate.shift(RIGHT * 5))

        prob_if_dis = Tex("you would test +\n\nif you had the disease").next_to(formula[0][7], UP * 4)
        for i in range(0,13):
            prob_if_dis[0][i].set_color(ORANGE)
        for i in range(15,len(prob_if_dis[0])):
            prob_if_dis[0][i].set_color(GREEN)
        arr3 = Arrow(start= prob_if_dis[0][-10].get_bottom(), end= formula[0][10].get_top())

        self.play(Write(formula[0][13]))
        for i in range(7,10):
            self.play(Write(formula[0][i]), run_time= 0.3)
        for i in range(0,13):
            self.play(Write(prob_if_dis[0][i]), run_time= 0.2)
        self.wait(1)
        for i in range(10,13):
            self.play(Write(formula[0][i]), run_time= 0.3)
        for i in range(13,len(prob_if_dis[0])):
            self.play(Write(prob_if_dis[0][i]), run_time= 0.2)
        self.play(Create(arr3))
        self.wait(2)
        self.play(FadeOut(VGroup(prob_if_dis, arr3)))

        prob_test_pos = Tex("probability of testing +").next_to(formula[0][-2], DOWN * 5)
        for i in range(14,len(prob_test_pos[0])):
            prob_test_pos[0][i].set_color(ORANGE)
        arr4 = Arrow(start= prob_test_pos.get_top(), end= formula[0][-2].get_bottom(), color= ORANGE)

        for i in range(18,len(formula[0])):
            self.play(Write(formula[0][i]), run_time= 0.3)
        self.wait(1)
        self.play(Write(prob_test_pos), Create(arr4))
        self.wait(2)
        self.play(FadeOut(VGroup(prob_test_pos, arr4)))



        formula1 = MathTex(r"P(H|E) = \frac{P(E|H)\times P(H)}{P(H)\times P(E|H)+P(-H)\times P(E|-H)}").move_to(formula[0][-2].get_center())
        formula1[0][2].set_color(GREEN)
        formula1[0][4].set_color(ORANGE)
        formula1[0][9].set_color(ORANGE)
        formula1[0][11].set_color(GREEN)
        formula1[0][16].set_color(GREEN)
        formula1[0][21].set_color(GREEN)
        formula1[0][26].set_color(ORANGE)
        formula1[0][28].set_color(GREEN)
        formula1[0][33:35].set_color(GREEN)
        formula1[0][-2].set_color(GREEN)
        formula1[0][-3].set_color(GREEN)
        formula1[0][-5].set_color(ORANGE)
        self.play(ReplacementTransform(formula, formula1), run_time= 1)
        
        ques_mark = Tex("?").next_to(formula1[0][16], UP)
        fre_dis = Tex("frequency of\n\nthe disease").next_to(formula[0][16], UP * 4)
        self.play(Write(ques_mark))
        self.wait(1)
        self.play(ReplacementTransform(ques_mark, fre_dis))
        self.wait(2)
        self.play(FadeOut(fre_dis))

        numbers = MathTex(r"P(H|E)=\frac{.99\times .001}{.001\times .99 + .999 \times 0.1}")
        numbers[0][2].set_color(GREEN)
        numbers[0][4].set_color(ORANGE)
        self.play(ReplacementTransform(formula1, numbers))
        self.wait(1)
        result = MathTex(r"P(H|E)=9\%")
        result[0][2].set_color(GREEN)
        result[0][4].set_color(GREEN)
        result_bayes = Tex("According to bayes theorem\n\nThere's only 9\% chance of having the disease\n\nafter testing positive\n\nwhich is comparatively really low what we estimated (i.e. 99\%)").next_to(result, DOWN  )
        for i in range(23,60):
            result_bayes[0][i].set_color(GREEN)
        for i in range(60,60+20):
            result_bayes[0][i].set_color(ORANGE)
        self.play(ReplacementTransform(numbers, result))
        self.wait(1)
        self.play(Write(result_bayes))

        """

        question = Tex("The number of balls in three urns is as follows:")

        table = Table(
            [["Urn #", "ORANGE", "White", "Black"],
            ["1","3", "2", "1"],
            ["2","2", "1", "2"],
            ["3","4", "2", "3"]],
            row_labels=[Text("R1"), Text("R2")],
            col_labels=[Text("C1"), Text("C2")])
        ent = table.get_entries_without_labels()

        self.add(table)