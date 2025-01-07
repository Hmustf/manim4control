from manim import *
from manim import config

config.pixel_width = 3840
config.pixel_height = 2160
config.frame_rate = 30  # Set your desired FPS

class SVGScene(Scene):
    def construct(self):
        # Load the SVG file
        svg = SVGMobject("scene1.svg")
        
        # Optionally, you can scale, move, or rotate the SVG
        svg.scale(4)  # Scale the SVG by a factor of 2
        svg.move_to(ORIGIN)  # Move the SVG to the center of the scene

        # Add the SVG to the scene
        self.add(svg)

        # Optionally, you can animate the SVG with a slower speed
        self.play(DrawBorderThenFill(svg), run_time=5)  # Set run_time to 5 seconds
        self.wait(10)
        self.play(Uncreate(svg), run_time=15)
        self.wait(2)

class SVGScene2(Scene):
    def construct(self):
        # Load the SVG file
        svg = SVGMobject("scene_2.svg")
        
        # Optionally, you can scale, move, or rotate the SVG
        svg.scale(4)  # Scale the SVG by a factor of 2
        svg.move_to(ORIGIN)  # Move the SVG to the center of the scene

        # Add the SVG to the scene
        self.add(svg)

        # Optionally, you can animate the SVG with a slower speed
        self.play(DrawBorderThenFill(svg), run_time=30)  # Set run_time to 5 seconds
        self.wait(10)
        self.play(FadeOut(svg), run_time=2)
        self.wait(2)
    
class SVGScene3(Scene):
    def construct(self):
        # Load the SVG file
        svg = SVGMobject("scene_3.svg")
        
        # Optionally, you can scale, move, or rotate the SVG
        svg.scale(4)  # Scale the SVG by a factor of 2
        svg.move_to(ORIGIN)  # Move the SVG to the center of the scene

        # Add the SVG to the scene
        self.add(svg)

        # Optionally, you can animate the SVG with a slower speed
        self.play(ShowIncreasingSubsets(svg), run_time=5)  # Set run_time to 5 seconds
        self.wait(10)
        self.play(FadeOut(svg), run_time=15)
        self.wait(2)

class SVGScene4(Scene):
    def construct(self):
        # Load the SVG file
        svg = SVGMobject("svg/vid1_scene1-04.svg")
        
        # Optionally, you can scale, move, or rotate the SVG
        svg.scale(4)  # Scale the SVG by a factor of 2
        svg.move_to(ORIGIN)  # Move the SVG to the center of the scene

        # Add the SVG to the scene
        self.add(svg)

        # Optionally, you can animate the SVG with a slower speed
        self.play(DrawBorderThenFill(svg), run_time=5)  # Set run_time to 5 seconds
        self.wait(10)
        self.play(FadeOut(svg), run_time=5)
        self.wait(2)

class SVGScene5(Scene):
    def construct(self):
        # Load the SVG file
        svg = SVGMobject("svg/vid1_scene1-05.svg")
        
        # Optionally, you can scale, move, or rotate the SVG
        svg.scale(4)  # Scale the SVG by a factor of 2
        svg.move_to(ORIGIN)  # Move the SVG to the center of the scene

        # Add the SVG to the scene
        self.add(svg)

        # Optionally, you can animate the SVG with a slower speed
        self.play(ShowIncreasingSubsets(svg), run_time=5)  # Set run_time to 5 seconds
        self.wait(10)
        self.play(FadeOut(svg), run_time=5)
        self.wait(2)

class SVGScene6(Scene):
    def construct(self):
        # Load the SVG file
        svg = SVGMobject("svg/vid1_scene1-06.svg")
        
        # Optionally, you can scale, move, or rotate the SVG
        svg.scale(3)  # Scale the SVG by a factor of 2
        svg.move_to(ORIGIN)  # Move the SVG to the center of the scene

        # Add the SVG to the scene
        self.add(svg)

        # Optionally, you can animate the SVG with a slower speed
        self.play(ShowIncreasingSubsets(svg), run_time=5)  # Set run_time to 5 seconds
        self.wait(10)
        self.play(FadeOut(svg), run_time=5)
        self.wait(2)

class SVGScene7(Scene):
    def construct(self):
        # Load the SVG file
        svg = SVGMobject("svg/vid1_scene1-07.svg")
        
        # Optionally, you can scale, move, or rotate the SVG
        svg.scale(4)  # Scale the SVG by a factor of 2
        svg.move_to(ORIGIN)  # Move the SVG to the center of the scene

        # Add the SVG to the scene
        self.add(svg)

        # Optionally, you can animate the SVG with a slower speed
        self.play(ShowIncreasingSubsets(svg), run_time=30)  # Set run_time to 5 seconds
        self.wait(10)
        self.play(FadeOut(svg), run_time=5)
        self.wait(2)

class SVGScene11(Scene):
    def construct(self):
        # Load the SVG file
        svg = SVGMobject("svg/vid1_scene1-01.svg")
        
        # Optionally, you can scale, move, or rotate the SVG
        svg.scale(4)  # Scale the SVG by a factor of 2
        svg.move_to(ORIGIN)  # Move the SVG to the center of the scene

        # Add the SVG to the scene
        self.add(svg)

        # Optionally, you can animate the SVG with a slower speed
        self.play(Create(svg), run_time=5)  # Set run_time to 5 seconds
        self.wait(10)
        self.play(FadeOut(svg), run_time=5)
        self.wait(2)

class TransformSVGScene(Scene):
    def construct(self):
        # Load the first SVG file
        svg1 = SVGMobject("test1.svg")
        svg1.move_to(ORIGIN)
        svg1.scale(3)

        # Load the second SVG file
        svg2 = SVGMobject("test2.svg")
        svg2.move_to(ORIGIN)
        svg2.scale(3)

        # Add the first SVG to the scene
        self.add(svg1)
        self.play(DrawBorderThenFill(svg1), run_time=1)  # Set run_time to 5 seconds
        self.wait(2)

        # Loop between both SVGs
        original_svg1 = svg1.copy()  # Store original state
        for _ in range(5):
            self.play(Transform(svg1, svg2), run_time=0.5,rate_func=smooth,path_arc=PI/2)
            self.play(Transform(svg1, original_svg1), run_time=0.5,rate_func=smooth,path_arc=PI/2)
        self.wait(2)