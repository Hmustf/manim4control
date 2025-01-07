from manim import *
from manim import config

config.pixel_width = 3840
config.pixel_height = 2160
config.frame_rate = 30

class TwoXEquation(Scene):
    def construct(self):
        # Create the equation
        equation = MathTex(
            "f(x)", "=", "2", "x",
            font_size=96
        )
        equation.set_color_by_tex_to_color_map({
            "y": GREEN,
            "2": GREEN,
            "x": GREEN,
            "=": GREEN
        })
        
        # Center the equation
        equation.move_to(ORIGIN)
        
        # Animation sequence
        self.play(
            Write(equation[0]),  # y
            run_time=1
        )
        self.play(
            Write(equation[1]),  # =
            run_time=0.5
        )
        self.play(
            Write(equation[2]),  # 2
            run_time=1
        )
        self.play(
            Write(equation[3]),  # x
            run_time=1
        )
        
        self.wait(2) 



class XSquaredEquation(Scene):
    def construct(self):
        # Create the equation
        equation = MathTex(
            "f(x)", "=", "x", "^", "2",
            font_size=96
        )
        equation.set_color_by_tex_to_color_map({
            "y": RED,
            "x": RED,
            "^": RED,
            "2": RED,
            "=": RED
        })
        
        # Center the equation
        equation.move_to(ORIGIN)
        
        # Animation sequence
        self.play(
            Write(equation[0]),  # y
            run_time=1
        )
        self.play(
            Write(equation[1]),  # =
            run_time=0.5
        )
        self.play(
            Write(equation[2]),  # 2
            run_time=1
        )
        self.play(
            Write(equation[3:]),  # x^2 
            run_time=1
        )
        
        self.wait(2) 