from manim import *

class EconomicsBayes(Scene):
    def construct(self):
        Tex.set_default(font_size= 25, color= YELLOW)
        Line.set_default(color= BLUE)

        title = Title("Scenario", font_size= 45, color= BLUE, match_underline_width_to_text= True)
        company = SVGMobject("company.svg").scale(0.4).to_corner(LEFT)
        economy = SVGMobject("economy.svg").scale(0.4).next_to(company, RIGHT, buff= 2)
        cte = Line(company.get_right(), economy.get_left())
        thinks = Tex("Hypothesize", font_size= 25, color= YELLOW).next_to(cte.get_center(), UP, buff= 0.1)
        ewe = Tex("5\% probability\n\nEconomy will expand.", font_size= 25).next_to(economy, DOWN)
        
        economy_expanded = economy.copy().scale(2).next_to(economy, RIGHT, buff= 3).shift(UP * 1.5)
        economy_unexpanded = economy.copy().next_to(economy , RIGHT, buff= 3.4).shift(DOWN * 1.5 )

        letee = Line(economy.get_right(), economy_expanded.get_left())
        etee = Tex("If economy expands").rotate(letee.get_angle()).next_to(letee.get_center(), UP, buff= 0.1)

        leteu = Line(economy.get_right(), economy_unexpanded.get_left())
        eteu = Tex("If economy doesn't expands").rotate(leteu.get_angle()).next_to(leteu.get_center(), DOWN, buff= 0.1)

        company_expanded = company.copy().scale(2).next_to(economy_expanded, RIGHT, buff= 3.9)
        company_unexpanded = company.copy().scale(1.5).next_to(economy_unexpanded, RIGHT, buff= 4.7)

        leetce = Line(economy_expanded.get_right(), company_expanded.get_left())
        eetce = Tex("90\%").next_to(leetce, UP, buff= 0.1)

        company_revenue = Tex("Company Revenue Increase Probability").next_to(leetce, DOWN, buff= 1.5)

        leutcu = Line(economy_unexpanded.get_right(), company_unexpanded.get_left())
        eutcu = Tex("40\%").next_to(leutcu, UP, buff= 0.1)


        # # self.add(company, economy, cte, thinks, ewe, economy_expanded, economy_unexpanded, letee, etee, leteu, eteu, company_expanded, company_unexpanded, leetce, leutcu, eetce, eutcu, company_revenue)

        self.play(Write(title))
        self.wait(2)
        self.play(Create(company), run_time= 2)
        self.wait(2)
        self.play(Create(cte), Write(thinks), run_time= 2)
        self.wait(2)
        self.play(Create(economy), Write(ewe), run_time= 2)
        self.wait(1)
        self.play(Create(letee), Write(etee), run_time= 2)
        self.play(Create(economy_expanded), run_time= 2)
        self.wait(2)
        self.play(FadeOut(ewe), run_time= 2)
        self.play(Create(leteu), Write(eteu), run_time= 2)
        self.play(Create(economy_unexpanded), run_time= 2)
        self.wait(2)
        self.play(Write(company_revenue), run_time= 2)
        self.play(Create(leetce), Write(eetce), run_time= 2)
        self.play(Create(company_expanded), run_time= 2)
        self.wait(2)
        self.play(Create(leutcu), Write(eutcu), run_time= 2)
        self.play(Create(company_unexpanded), run_time= 2)
        self.wait(2)

        self.play(FadeOut(VGroup(company, economy, cte, thinks, economy_expanded, economy_unexpanded, letee, etee, leteu, eteu, company_expanded, company_unexpanded, leetce, leutcu, eetce, eutcu, company_revenue)))
        
        self.wait(1)


        title1 = Title("Probability the Economy has expanded given Company's Revenu has risen", font_size= 40, match_underline_width_to_text= True)

        Tex.set_default(font_size= 35)
        MathTex.set_default(font_size= 35)
        statement = Tex("We want to find out:").to_corner(LEFT).shift(UP * 2.5)
        statement1 = MathTex("P\ (\ Economy\ Expression\ |\ Company\ Revenue\ Rises)\ =\ P\ (\ EE\ |\ RR\ )").next_to(statement, DOWN, aligned_edge= LEFT)
        statement2 = MathTex(r"P\ (\ EE\ |\ RR\ )\ =\ P\ (\ RR\ |\ EE\ )\ \times \frac{P(EE)}{P(RR)}").next_to(statement1, DOWN, aligned_edge= LEFT)
        statement3 = MathTex("P\ (\ Economy\ Expansion\ )\ =\ P\ (\ EE\ )\ =\ 0.05").next_to(statement2, DOWN, aligned_edge= LEFT)
        statement4 = MathTex("P\ (\ Revenue\ Rise\ |\ Economy\ Expansion\ )\ =\ P\ (\ RR\ |\ EE\ )\ =\ 0.09").next_to(statement3, DOWN, aligned_edge=LEFT)
        statement5 = MathTex(r"P\ (\ Revenue\ Rise\ )\ =\ P(RR)\ = 0.05\times 0.90\ +\ 0.95\times \ 0.40\ =\ 0.425").next_to(statement4, DOWN, aligned_edge= LEFT)
        statement6 = MathTex(r"P(EE\ |\ RR)\ =\ 0.90\times \frac{0.05}{0.425}\ =\ 0.106").next_to(statement5, DOWN, aligned_edge= LEFT)

        result = Tex("If the company's revenue has risen, then there is a 10.6\% probability that the economy has expanded").to_corner(DOWN)
        result[0][42:47].set_color(RED)

        # self.add(title1, statement, statement1, statement2, statement3, statement4,statement5, statement6, result)

        self.play(ReplacementTransform(title, title1), run_time= 2)
        self.wait(2)
        self.play(Write(statement), run_time= 2)
        self.wait(2)
        self.play(Write(statement1), run_time= 2)
        self.wait(2)
        self.play(Write(statement2), run_time= 2)
        self.wait(2)
        self.play(Write(statement3), run_time= 2)
        self.wait(2)
        self.play(Write(statement4), run_time= 2)
        self.wait(2)
        self.play(Write(statement5), run_time= 2)
        self.wait(2)
        self.play(Write(statement6), run_time= 2)
        self.wait(2)
        self.play(Write(result), run_time= 2)
        self.wait(2)