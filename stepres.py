from manim import *
from scipy.signal import TransferFunction, step
import numpy as np
from manim import config

config.pixel_width = 3840
config.pixel_height = 2160
config.frame_rate = 30  # Set your desired FPS

class TransferFunctionStepResponses(Scene):
    def construct(self):
        # Create axes for the plot with grid
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 2, 0.2],
            axis_config={"include_numbers": True},
            x_length=12,
            y_length=7,
        ).center()

        # Add grid
        grid = NumberPlane(
            x_range=[0, 10, 1],
            y_range=[0, 2, 0.2],
            x_length=12,
            y_length=7,
            background_line_style={
                "stroke_color": GRAY_D,
                "stroke_width": 0.5,
                "stroke_opacity": 0.3
            }
        ).center()

        self.play(
            Create(axes),
            run_time=1
        )

        # Define parameters
        omega_n = 2.0
        zeta_values = [0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]
        colors = color_gradient([BLUE, GREEN, YELLOW, ORANGE, RED], len(zeta_values))

        # Plot responses
        t = np.linspace(0, 10, 1000)
        
        # Create a list to store all response curves
        response_curves = []
        
        # Plot each curve individually with slower animation
        for zeta, color in zip(zeta_values, colors):
            num = [omega_n**2]
            den = [1, 2 * zeta * omega_n, omega_n**2]
            system = TransferFunction(num, den)
            _, response = step(system, T=t)

            response_curve = axes.plot_line_graph(
                x_values=t,
                y_values=response,
                line_color=color,
                add_vertex_dots=False,
                stroke_width=2,
            )
            
            response_curves.append(response_curve)  # Store each curve
            
            self.play(
                Create(response_curve),
                run_time=1.5
            )

        self.wait(2)
        
        # Create an animation group to remove everything
        self.play(
            *[Uncreate(curve) for curve in response_curves],
            Uncreate(axes),
            run_time=3
        )

        self.wait(1)

        