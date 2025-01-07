from manim import *
import random

from manim import config

config.pixel_width = 3840
config.pixel_height = 2160
config.frame_rate = 30  # Set your desired FPS

class PoleZeroMapScene(Scene):
    def construct(self):
        # Create the complex plane
        plane = ComplexPlane(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            background_line_style={
                "stroke_opacity": 0.6,
                "stroke_width": 1,
            }
        )

        # Add labels
        plane.add_coordinates()
        
        # Create title
        title = Text("Pole-Zero Map").scale(0.8).to_edge(UP)
        
        # Define initial poles and zeros
        poles = [
            [-2, 1],   # Complex pole
            [-2, -1],  # Complex conjugate pole
            [-1, 0],   # Real pole
        ]
        zeros = [
            [1, 0],    # Real zero
        ]
        
        # Create pole and zero markers
        pole_markers = VGroup(*[
            Cross(stroke_width=3).scale(0.2).move_to(plane.c2p(p[0], p[1]))
            for p in poles
        ]).set_color(RED)
        
        zero_markers = VGroup(*[
            Circle(radius=0.1, stroke_width=3).move_to(plane.c2p(z[0], z[1]))
            for z in zeros
        ]).set_color(BLUE)

        # Group plane and markers together and scale
        plot_group = VGroup(plane, pole_markers, zero_markers).scale(0.7)

        # Add legend
        legend = VGroup(
            VGroup(
                Cross(stroke_width=3).scale(0.2).set_color(RED),
                Text("Poles", font_size=24).set_color(RED)
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                Circle(radius=0.1, stroke_width=3).set_color(BLUE),
                Text("Zeros", font_size=24).set_color(BLUE)
            ).arrange(RIGHT, buff=0.2)
        ).arrange(DOWN, aligned_edge=LEFT).next_to(plane, RIGHT)

        # Initial animation sequence
        self.play(Create(plot_group))
        self.play(Create(legend))
        self.wait(1)

        # Function to generate random positions
        def get_random_position():
            x = random.uniform(-4, 4)
            y = random.uniform(-4, 4)
            return plane.c2p(x, y)

        # Animate random movements
        # Each iteration takes 3 seconds (2s animation + 0.5s wait + 0.5s buffer)
        # For 1 minute, we need approximately 20 iterations (60 seconds / 3 seconds)
        for _ in range(20):  
            # Generate new random positions
            new_positions_poles = [get_random_position() for _ in range(len(poles))]
            new_position_zero = get_random_position()
            
            # Create animations for conjugate poles (keeping them conjugate)
            animations = []
            
            # Move first pole randomly
            animations.append(pole_markers[0].animate.move_to(new_positions_poles[0]))
            
            # Move second pole to conjugate position of first pole
            new_pos = plane.p2c(new_positions_poles[0])
            conjugate_pos = plane.c2p(new_pos[0], -new_pos[1])
            animations.append(pole_markers[1].animate.move_to(conjugate_pos))
            
            # Move real pole randomly
            animations.append(pole_markers[2].animate.move_to(new_positions_poles[2]))
            
            # Move zero randomly
            animations.append(zero_markers[0].animate.move_to(new_position_zero))
            
            # Play all animations together
            self.play(
                *animations,
                run_time=2,
                rate_func=smooth
            )
            self.wait(0.5)

            

        self.wait(1)
        self.play(Uncreate(plot_group))
        self.play(Uncreate(legend))
        self.wait(1)
