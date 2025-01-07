from manim import *
import numpy as np
import control

class StepResponseScene(Scene):
    def construct(self):
        # System parameters
        NATURAL_FREQUENCY = 1.0
        DAMPING_RATIO = 0.5

        # Create transfer function
        numerator = [NATURAL_FREQUENCY**2]
        denominator = [1, 2 * DAMPING_RATIO * NATURAL_FREQUENCY, NATURAL_FREQUENCY**2]
        G = control.TransferFunction(numerator, denominator)

        # Get step response data with more points for smoother curve
        t = np.linspace(0, 8, 1000)
        t, y = control.step_response(G, T=t)
        info = control.step_info(G)

        # Create axes
        axes = Axes(
            x_range=[-0.2, 8, 1],
            y_range=[-0.1, 1.5, 0.5],
            axis_config={"color": BLUE},
            x_axis_config={"numbers_to_include": np.arange(0, 9, 2)},
            y_axis_config={"numbers_to_include": np.arange(0, 1.6, 0.5)},
            tips=False
        )

        # Add labels
        x_label = axes.get_x_axis_label("Time (s)")
        y_label = axes.get_y_axis_label("Amplitude")
        labels = VGroup(x_label, y_label)

        # Create the step response curve using pre-calculated points
        points = [axes.coords_to_point(t_val, y_val) for t_val, y_val in zip(t, y)]
        step_response = VMobject(color=BLUE)
        step_response.set_points_smoothly(points)

        # Create steady state line
        steady_state = DashedLine(
            axes.c2p(0, 1),
            axes.c2p(8, 1),
            color=RED,
            dash_length=0.1
        )

        # Create title
        title = Text("Second-Order System Step Response", font_size=36)
        title.to_edge(UP)

        # Animation sequence
        self.play(Write(title))
        self.play(Create(axes), Create(labels))
        self.wait()
        
        # Animate the step response curve
        self.play(Create(step_response), run_time=2)
        self.play(Create(steady_state))
        
        # Add settling bounds (±2%)
        upper_bound = DashedLine(
            axes.c2p(0, 1.02),
            axes.c2p(8, 1.02),
            color=GRAY,
            dash_length=0.05
        )
        lower_bound = DashedLine(
            axes.c2p(0, 0.98),
            axes.c2p(8, 0.98),
            color=GRAY,
            dash_length=0.05
        )
        self.play(Create(upper_bound), Create(lower_bound))

        # Add key points and annotations
        peak_time = info['PeakTime']
        peak_value = info['Peak']
        rise_time = info['RiseTime']
        settling_time = info['SettlingTime']

        # Peak point
        peak_dot = Dot(axes.c2p(peak_time, peak_value), color=WHITE)
        peak_label = MathTex("t_p").next_to(peak_dot, UR, 0.1)
        
        # Rise time point
        rise_dot = Dot(axes.c2p(rise_time, 0.632), color=WHITE)
        rise_label = MathTex("t_r").next_to(rise_dot, UR, 0.1)
        
        # Settling time line
        settling_line = Line(
            axes.c2p(settling_time, 0.98),
            axes.c2p(settling_time, 1.02),
            color=GRAY
        )
        settling_label = MathTex("t_s").next_to(settling_line, RIGHT, 0.1)

        # Animate points and labels
        self.play(
            Create(peak_dot), Write(peak_label),
            Create(rise_dot), Write(rise_label),
            Create(settling_line), Write(settling_label)
        )

        # Add overshoot annotation
        overshoot_arrow = Arrow(
            axes.c2p(peak_time, 1),
            axes.c2p(peak_time, peak_value),
            color=RED,
            buff=0
        )
        overshoot_label = MathTex("PO").next_to(overshoot_arrow, RIGHT, 0.1)
        
        self.play(Create(overshoot_arrow), Write(overshoot_label))
        
        # Final pause
        self.wait(2) 