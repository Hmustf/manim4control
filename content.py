from manim import *

class SVGScene(Scene):
    def construct(self):
        # Load the SVG file
        svg = SVGMobject("svg/content_1.svg")
        
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

class SVGScene2(Scene):
    def construct(self):
        # Load the SVG file
        svg = SVGMobject("svg/content.svg")
        
        # Optionally, you can scale, move, or rotate the SVG
        svg.scale(4)  # Scale the SVG by a factor of 2
        svg.move_to(ORIGIN)  # Move the SVG to the center of the scene

        # Add the SVG to the scene
        self.add(svg)

        # Optionally, you can animate the SVG with a slower speed
        self.play(DrawBorderThenFill(svg), run_time=30)  # Set run_time to 5 seconds
        self.wait(10)
        self.play(FadeOut(svg), run_time=5)
        self.wait(2)



class Example(ZoomedScene):  
    def __init__(self, **kwargs):   #HEREFROM
        ZoomedScene.__init__( 
            self, 
            zoom_factor=0.1, 
            zoomed_display_height=6, 
            zoomed_display_width=3,  
            image_frame_stroke_width=20,  
            zoomed_camera_config={  
                'default_frame_stroke_width': 3,  
            },  
            **kwargs  
        )      
      
    def construct(self):  
        self.activate_zooming(animate=False)  
      
        ax = Axes(  
            x_range=[0, 10, 2],  
            y_range=[0,10, 2],  
            x_length=2,  
            y_length=2,  
            x_axis_config={'color': ORANGE},  
            y_axis_config={'color': ORANGE},  
        )  
        ax.shift(DL)  
        x_vals = [0, 1, 2, 3,4,5]  
        y_vals = [2, -1, 4, 2, 4, 1]  
        graph = ax.plot_line_graph(x_values=x_vals, y_values=y_vals)  
        self.zoomed_camera.frame.move_to(graph.get_top()+0.1*DL)  
        self.zoomed_display.shift(3*LEFT+0.4*UP)  
        self.camera.frame.scale(1/2)  
        self.camera.frame.shift(UR*1)  
        self.add(ax, graph)  #HERETO