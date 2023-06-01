from manim import *

class bayes(Scene):
    def construct(self):
        # Adding Text like title and virus detection
        medical_test = Title("Medical Test", match_underline_width_to_text= True).to_edge(UL)
        virus_detected = Tex(f"Virus\n\nDetected", font_size= 40)
        for i in range(5,13):
            virus_detected[0][i].set_color(YELLOW)
        virus_detected.add_background_rectangle(color= "#4dffc3", opacity= 0.5)
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
                dots[i].set_color("#ff4d4d")
                dots[i].add(plus)
                
            else:
                negative = Tex("-", font_size= 40).shift(dots[i].get_center())
                dots[i].set_color("#4dffc3")
                dots[i].add(negative)
        self.play(FadeOut(a))                

        self.play(virus_detected.animate.move_to(ORIGIN))

        tested_truely = Rectangle(height= 2.5, width= 4, fill_color= "#dffff4", fill_opacity= 0.5).next_to(RIGHT * 2.5 + UP * 1.8)
        t = Tex("Tested Truly").next_to(tested_truely, UP)
        tested_truely.add(t)
        tested_falsely = Rectangle(height= 2.5, width= 4, fill_color= "#f6c4ce", fill_opacity= 0.5).next_to(tested_truely, DOWN, buff= 1.3)
        t = Tex("Tested False").next_to(tested_falsely, UP)
        tested_falsely.add(t)
        self.add(tested_truely, tested_falsely)



        pre = dots[0]
        n = 0
        self.play(pre.animate.scale(0.8).move_to(tested_truely.get_left()).shift(UP * 0.65 + RIGHT * 0.2), run_time= 0.1)
        for i in range(1,int(len(dots)/2) + 3):
            if i%13 != 0:
                self.play(dots[i].animate.scale(0.8).next_to(pre, RIGHT, buff= 0.1), run_time= 0.1)
                self.add(dots[i])
            elif i%13 == 0:
                self.play(dots[i].animate.scale(0.8).next_to(dots[i-13], DOWN, buff= 0.2), run_time= 0.1)
                self.add(dots[i])
            pre = dots[i]
            n = i

        self.play(dots[n+1].animate.scale(0.8).move_to(tested_falsely.get_left()).shift(UP * 0.65 + RIGHT * 0.2), run_time= 0.5)

        for i in range(n+2, len(dots)):
            if i%13 != 0:
                self.play(dots[i].animate.scale(0.8).next_to(pre, RIGHT, buff= 0.1), run_time= 0.1)
                self.add(dots[i])
            elif i%13 == 0:
                self.play(dots[i].animate.scale(0.8).next_to(dots[i-13], DOWN, buff= 0.2), run_time= 0.1)
                self.add(dots[i])
            pre = dots[i]
            n = i

        ques = Tex(f"If you test positive\n\nfor the test what\n\nis the probability that\n\nyou have the disease?\n\n").shift(LEFT * 4)
        ans = Tex(f"Well a common answer\n\nmay be 99\% because\n\nthe accuracy of the\n\ntest is 99\%.", color= GREEN).next_to(ques, DOWN)
        # self.add(ques, ans)
        self.wait(10)
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
        formula[0][2].set_color(YELLOW)
        formula[0][4].set_color(ORANGE)
        formula[0][9].set_color(ORANGE)
        formula[0][11].set_color(YELLOW)
        formula[0][16].set_color(YELLOW)
        formula[0][21].set_color(ORANGE)
        # self.add(formula)
        for i in range(0,3):
            self.play(Write(formula[0][i]), run_time= 0.3)

        act_have = Tex("actually have\n\nthe disease", color= YELLOW).next_to(formula[0][0].get_center(), UP * 6)
        arr = Arrow(start= act_have[0][13].get_bottom(), end= formula[0][2].get_top(), color= YELLOW)
        given = Tex("given").next_to(act_have[0][20], DOWN, buff= 0.1)

        self.play(Write(act_have), Create(arr), run_time= 0.8)
        self.wait(1.5)
        self.play(Write(given))

        tested_pos = Tex("you tested +", color= ORANGE).next_to(formula[0][3].get_center(), DOWN * 7)
        arr1 = Arrow(start= tested_pos[0][3].get_top(), end= formula[0][4].get_bottom(), color= ORANGE)

        for i in range(3,6):
            self.play(Write(formula[0][i]), run_time= 0.3)
        self.play(Write(tested_pos), Create(arr1), run_time= 1.5)
        self.wait(2)
        self.play(FadeOut(VGroup(act_have, arr, given, tested_pos, arr1)))

        prior_prob = Tex("PRIOR probability of\n\nhaving\n\nthe disease").next_to(formula[0][-7], UP  * 7)
        for i in range(18,len(prior_prob[0])):
            prior_prob[0][i].set_color(YELLOW)
        arr2 = Arrow(start= prior_prob.get_bottom(), end= formula[0][-7].get_top(), color= YELLOW)

        self.play(Write(formula[0][6]), run_time= 1)
        for i in range(14,18):
            self.play(Write(formula[0][i]))
        self.play(bayes_theorm.animate.shift(LEFT * 5), run_time= 1.5)
        self.play(Write(prior_prob), Create(arr2), run_time= 1.5)
        self.wait(2)
        self.play(FadeOut(VGroup(prior_prob, arr2)))
        self.play(bayes_theorm.animate.shift(RIGHT * 5), run_time= 1.5)

        prob_if_dis = Tex("you would test +\n\nif you had the disease").next_to(formula[0][7], UP * 4)
        for i in range(0,13):
            prob_if_dis[0][i].set_color(ORANGE)
        for i in range(15,len(prob_if_dis[0])):
            prob_if_dis[0][i].set_color(YELLOW)
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
        self.play(Create(arr3), run_time= 1.5)
        self.wait(2)
        self.play(FadeOut(VGroup(prob_if_dis, arr3)))

        prob_test_pos = Tex("probability of testing +").next_to(formula[0][-2], DOWN * 5)
        for i in range(14,len(prob_test_pos[0])):
            prob_test_pos[0][i].set_color(ORANGE)
        arr4 = Arrow(start= prob_test_pos.get_top(), end= formula[0][-2].get_bottom(), color= ORANGE)

        for i in range(18,len(formula[0])):
            self.play(Write(formula[0][i]), run_time= 0.3)
        self.wait(1)
        self.play(Write(prob_test_pos), Create(arr4), run_time= 1.5)
        self.wait(2)
        self.play(FadeOut(VGroup(prob_test_pos, arr4)))



        formula1 = MathTex(r"P(H|E) = \frac{P(E|H)\times P(H)}{P(H)\times P(E|H)+P(-H)\times P(E|-H)}").move_to(formula[0][-2].get_center())
        formula1[0][2].set_color(YELLOW)
        formula1[0][4].set_color(ORANGE)
        formula1[0][9].set_color(ORANGE)
        formula1[0][11].set_color(YELLOW)
        formula1[0][16].set_color(YELLOW)
        formula1[0][21].set_color(YELLOW)
        formula1[0][26].set_color(ORANGE)
        formula1[0][28].set_color(YELLOW)
        formula1[0][33:35].set_color(YELLOW)
        formula1[0][-2].set_color(YELLOW)
        formula1[0][-3].set_color(YELLOW)
        formula1[0][-5].set_color(ORANGE)
        self.play(ReplacementTransform(formula, formula1), run_time= 1)
        
        ques_mark = Tex("?").next_to(formula1[0][16], UP)
        fre_dis = Tex("frequency of\n\nthe disease").next_to(formula[0][16], UP * 4)
        self.play(Write(ques_mark), run_time= 1.5)
        self.wait(3)
        self.play(ReplacementTransform(ques_mark, fre_dis), run_time= 2)
        self.wait(3)
        self.play(FadeOut(fre_dis))
        self.wait(2)

        numbers = MathTex(r"P(H|E)=\frac{.99\times .001}{.001\times .99 + .999 \times 0.1}")
        numbers[0][2].set_color(YELLOW)
        numbers[0][4].set_color(ORANGE)
        self.play(ReplacementTransform(formula1, numbers), run_time= 2)
        self.wait(3)
        result = MathTex(r"P(H|E)=9\%")
        result[0][2].set_color(YELLOW)
        result[0][4].set_color(YELLOW)
        result_bayes = Tex("According to bayes theorem\n\nThere's only 9\% chance of having the disease\n\nafter testing positive\n\nwhich is comparatively low compared to the\n\ninitial statement (i.e. 99\%)").next_to(result, DOWN  )
        for i in range(23,60):
            result_bayes[0][i].set_color(YELLOW)
        for i in range(60,60+20):
            result_bayes[0][i].set_color(ORANGE)
        self.play(ReplacementTransform(numbers, result), run_time= 2)
        self.wait(3)
        self.play(Write(result_bayes), run_time= 3)
        self.wait(10)
        self.play(FadeOut(
            bayes_theorm,result, result_bayes
        ))

        

        question = Tex("The number of balls in three urns is as follows:").to_edge(UL)

        self.play(Write(question), run_time= 1.5)
        self.wait(1)

        table = Table(
            [["Urn #", "RED", "White", "Green"],
            ["1","3", "2", "1"],
            ["2","2", "1", "2"],
            ["3","4", "2", "3"]],
            row_labels=[Text("R1"), Text("R2"), Text("3"), Text("4")],
            col_labels=[Text("C1"), Text("C2"), Text("3"), Text("4")])
        ent = table.get_entries_without_labels().scale(0.5)
        ent[1].set_color(RED)
        for i in range(1,4):
            ent[i*4+1].set_color(RED)
        ent[3].set_color(GREEN)
        for i in range(1,4):
            ent[i*4+3].set_color(GREEN)
        ent.next_to(question[0][9], DOWN)
        # self.add(question,ent)
        self.play(Create(ent), run_time= 1.5)
        self.wait(2)

        question1 = Tex("One urn is chosen at random\n\nand two balls are drawn\n\nRed and White").next_to(ent, DOWN)
        self.play(Write(question1), run_time= 2)
        for i in range(41,41+3):
            question1[0][i].set_color(RED )
        b1 = Dot(color= RED).next_to(question1[0][42], DOWN)
        b2 = Dot(color= WHITE).next_to(question1[0][49], DOWN)
        balls = VGroup(b1, b2)#.next_to(question1, DOWN)
        # self.add( balls)?
        self.play(Create(balls), run_time= 1.5)
        self.wait(1)
        arrow = Arrow(start=ent[7].get_right(), end= ent[7].get_right() + RIGHT * 2.5)
        # self.add(arrow)
        self.play(AnimationGroup(
            Create(arrow),
            b2.animate.next_to(b1, RIGHT)
            ), run_time= 1.5)
        self.play(balls.animate.next_to(arrow.get_right(), RIGHT), run_time= 1.5)
        
        question2 = Tex("What is the probability\n\nthat they came from urn 1?", color= YELLOW, font_size= 40).next_to(balls, DOWN).shift(RIGHT * 1)
        self.play(Write(question2), run_time= 1.5)
        # self.add(question2)
        self.wait(2)

        self.play(FadeOut(question1))
        self.wait(1)

        P_u = MathTex(r"P(U_1) = P(U_2) = P(U_3) = \frac{1}{3}", font_size= 40)
        P_u[0][3].set_color(BLACK)
        P_u[0][9].set_color(BLACK)
        P_u[0][15].set_color(BLACK)
        n1 = ent[4].copy()
        n2 = ent[8].copy()
        n3 = ent[12].copy()

        for i in range(0,17):
            self.play(Write(P_u[0][i]), run_time= 0.2)
        self.play(AnimationGroup(
            n1.animate.move_to(P_u[0][3].get_center()).scale(0.7),
            n2.animate.move_to(P_u[0][9].get_center()).scale(0.7),
            n3.animate.move_to(P_u[0][15].get_center()).scale(0.7),
        ), run_time= 2)
        self.wait(1)
        for i in range(17,len(P_u[0])):
            self.play(Write(P_u[0][i]), run_time= 0.2)
        self.wait(1)

        pe1 = MathTex(r"P(E|U_1) : Event\ (Red,White\ |\ from\ urn\ 1) = \frac{^5C_1\times ^2C_1}{^6C_2}= \frac{2}{5}", font_size= 40).next_to(P_u, DOWN)
        pe1[0][4].set_color(BLACK)
        pe1[0][5].set_color(BLACK)
        for i in range(14,14+3):
            pe1[0][i].set_color(RED)
        # self.add(pe1)
        self.wait(3)

        for i in range(0,4):
            self.play(Write(pe1[0][i]), run_time= 0.2)
        u1 = VGroup(P_u[0][2], n1).copy()
        self.play(u1.animate.move_to(pe1[0][4].get_center()))
        for i in range(5,14):
            self.play(Write(pe1[0][i]), run_time= 0.2)
        self.play(AnimationGroup(
            FadeOut(arrow),
            b1.animate.move_to(pe1[0][15].get_center()),
            b2.animate.move_to(pe1[0][18].get_center()),
            Write(pe1[0][17]),
            run_time= 1.5
        ))
        self.wait(1)
        self.play(FadeOut(b1))
        for i in range(14,14+3):
            self.play(Write(pe1[0][i]), run_time= 0.2)
        self.play(FadeOut(b2))
        for i in range(18,18+5):
            self.play(Write(pe1[0][i]), run_time= 0.2)
        for i in range(23,len(pe1[0])-4):
            self.play(Write(pe1[0][i]), run_time= 0.2)

        pe2 = MathTex(r"P(E|U_2)\ :\ \frac{^2C_1\times ^1C_1}{^5C_2}=\frac{1}{5}", font_size= 40).next_to(pe1[0][6], DOWN, buff= 0.5)
        pe3 = MathTex(r"E(E|U_3)\ :\ \frac{^4C_1\times ^2C_2}{^9C_2}=\frac{2}{9}", font_size= 40).next_to(pe1[0][-6], DOWN, buff= 0.5)
        
        for i in range(0,len(pe2[0])-4):
            self.play(Write(pe2[0][i]), run_time= 0.2)
        self.wait(2)
        for i in range(0,len(pe2[0])-4):
            self.play(Write(pe3[0][i]), run_time= 0.2)
        self.wait(2)

        for i in range(len(pe1[0])-4, len(pe1[0])):
            self.play(Create(pe1[0][i]), run_time= 0.2)
        self.wait(2)
        for i in range(len(pe2[0])-4, len(pe2[0])):
            self.play(Create(pe2[0][i]), run_time= 0.2)
        self.wait(2)
        for i in range(len(pe3[0])-4, len(pe3[0])):
            self.play(Create(pe3[0][i]), run_time= 0.2)
        self.wait(2)

        question2.add_background_rectangle(color= GREEN)
        question2[0].scale(1.3)
        rec = Rectangle(height= question2[0].get_height(), width= question2[0].get_width()).shift(question2[0].get_center())
        question2.add(rec)
        self.play(Create(rec))
        self.play(
            FadeOut(question),
            FadeOut(ent),
            question2.animate.to_edge(UP),
            run_time= 1.5)
        self.play(VGroup(u1, n1, n2, n3, P_u, pe1, pe2, pe3).animate.shift(UP * 1.5), run_time= 1.5)
        

        pu = MathTex(r"P(U_1|E) = \frac{\frac{2}{5}}{\frac{2}{5}+\frac{1}{5}+\frac{2}{9}}=\frac{18}{37}", font_size= 35, color= BLACK).next_to(pe1, DOWN, buff= 2)
        for i in range(0,8):
            pu[0][i].set_color(WHITE)
        pu[0][11].set_color(WHITE)
        # self.wait(1)
        
        for i in range(9):
            self.play(Write(pu[0][i]), run_time= 0.2)
        self.play(Write(pu[0][11]))
        self.wait(1)
        f1 = pe1[0][len(pe1[0])-3:len(pe1[0])].copy()
        f2 = pe1[0][len(pe1[0])-3:len(pe1[0])].copy()
        f3 = pe2[0][len(pe2[0])-3:len(pe2[0])].copy()
        f4 = pe3[0][len(pe3[0])-3:len(pe3[0])].copy()

        self.play(AnimationGroup(
            f1.animate.move_to(pu[0][9].get_center()).scale(0.5),
            f2.animate.move_to(pu[0][13].get_center()).scale(0.5),
            pu[0][15].animate.set_color(WHITE),
            f3.animate.move_to(pu[0][17].get_center()).scale(0.5),
            pu[0][19].animate.set_color(WHITE),
            f4.animate.move_to(pu[0][21].get_center()).scale(0.5),
        ))
        self.wait(2)
        for i in range(23,len(pu[0])):
            self.play(pu[0][i].animate.set_color(WHITE), run_time= 1)
        self.wait(5)